from datetime import datetime, timedelta
from enum import Enum
from pathlib import PurePosixPath
from typing import Annotated, Dict, Iterator, List, Literal, Optional, Set, Union
from uuid import UUID

from pydantic import AfterValidator, BaseModel, Field

from extended_dataset_profile.models.version import SchemaVersion


class DataSpace(BaseModel):
    name: str = Field(description="Name of the dataspace")
    url: str = Field(description="URL of the dataspace")


class AssetProcessingStatus(str, Enum):
    original_data = "Original Data"
    processed_data = "Processed Data"
    refined_data = "Refined Data"
    ai_ml_result_data = "AI/ML Result Data"


class DataSetVolume(str, Enum):
    kb = "KB"
    mb = "MB"
    gb = "GB"
    tb = "TB"
    pb = "PB"


class DataSetFrequency(str, Enum):
    second = "second"
    minute = "minute"
    hour = "hour"
    day = "day"


class DataSetTransfer(str, Enum):
    static = "static"
    frequent = "inflationary"


class DataSetImmutability(str, Enum):
    immutable = "immutable"
    not_immutable = "not-immutable"


class DataSetType(str, Enum):
    structured = "structured"
    semi_structured = "semi-structured"
    image = "image"
    video = "video"
    audio = "audio"
    documents = "documents"


class DataSetCompression(str, Enum):
    none = "None"
    gzip = "gzip"
    zip = "zip"
    tar = "tar.gz"
    seven_zip = "7zip"


class TemporalConsistency(BaseModel):
    timeScale: str = Field(description="Time scale this temporal consistency has been tested for")
    differentAbundancies: int = Field(description="Number of unique values on given time resolution")
    stable: bool = Field(description="The value stays stable on the given time resolution")
    numberOfGaps: int = Field(description="Number of gaps at the given timescale")


Numeric = Union[int, float, timedelta, complex]

FileReference = PurePosixPath


class _BaseDataSet(BaseModel):
    uuid: UUID = Field(description="Identifier for the dataset")
    parentUuid: Optional[UUID] = Field(description="Reference to the identifier of the parent dataset, if any")
    name: PurePosixPath = Field(description="Name of the dataset")


class Augmentation(BaseModel):
    sourceColumns: List[str] = Field(description="List of source columns on which the augmented column is based")
    formula: Optional[str] = Field(
        default=None,
        description="The calculation that was applied to the source columns to create the augmented column",
    )
    parameters: List[str] = Field(default_factory=list, description="The parameters used for the calculation")


class AugmentedColumn(BaseModel):
    name: str = Field(description="Name of the augmented column")
    file: Optional[PurePosixPath] = Field(
        default=None,
        description="Path of the augmented file this column was added. If augmentedFile is None, EDPS will assume that the augmented column contained in all files.",
    )
    augmentation: Augmentation = Field(description="Augmentation information")


class _BaseColumn(BaseModel):
    name: str = Field(description="Name of the column")
    nonNullCount: int = Field(description="Number of non empty entries in the column")
    nullCount: int = Field(description="Number of empty entries in the column")
    numberUnique: int = Field(description="Number of unique values")
    augmentation: Optional[Augmentation] = Field(
        default=None, description="If this column was augmented this filed contains all relevant information"
    )


class TimeBasedGraph(BaseModel):
    timeBaseColumn: str
    file: FileReference


class NumericColumn(_BaseColumn):
    min: Numeric
    max: Numeric
    mean: Numeric
    median: Numeric
    stddev: Numeric
    upperPercentile: Numeric = Field(description="Value of the upper 1% quantile")
    lowerPercentile: Numeric = Field(description="Value of the lower 1% quantile")
    upperQuantile: Numeric = Field(description="Value of the upper 25% quantile")
    lowerQuantile: Numeric = Field(description="Value of the lower 25% quantile")
    percentileOutlierCount: int = Field(description="Number of elements in the lower or upper percentile")
    upperZScore: Numeric = Field(description="Value of the upper standard score")
    lowerZScore: Numeric = Field(description="Value of the lower standard score")
    zScoreOutlierCount: int = Field(description="Number of elements outside the lower and upper standard scores")
    upperIQR: Numeric = Field(description="Value of the upper limit of the inter quartile range (25%)")
    lowerIQR: Numeric = Field(description="Value of the lower limit of the inter quartile range (25%)")
    iqr: Numeric = Field(description="Value of the inter quartile range")
    iqrOutlierCount: int = Field(description="Number of elements outside of the inter quartile range")
    distribution: str = Field(description="The best fitting distribution for the data in this column")
    distributionGraph: Optional[FileReference] = Field(
        default=None, description="Link to the combined histogram/distribution graph"
    )
    boxPlot: FileReference = Field(description="Link to the box plot of this column")
    original_series: List[TimeBasedGraph] = Field(
        default_factory=list, description="Original data graphs over all available date time columns"
    )
    seasonalities: List[TimeBasedGraph] = Field(
        default_factory=list, description="Seasonality graphs oer all available date time columns"
    )
    trends: List[TimeBasedGraph] = Field(
        default_factory=list, description="Trend graphs over all available date time columns"
    )
    residuals: List[TimeBasedGraph] = Field(
        default_factory=list, description="Residual graphs over all available date time columns"
    )
    dataType: str


class TemporalCover(BaseModel):
    earliest: datetime
    latest: datetime


class DateTimeColumn(_BaseColumn):
    temporalCover: TemporalCover
    all_entries_are_unique: bool
    monotonically_increasing: bool
    monotonically_decreasing: bool
    periodicity: Optional[str] = Field(default=None, description="The main periodicity found for this column")
    temporalConsistencies: List[TemporalConsistency] = Field(description="Temporal consistency at given timescale")
    format: str = Field(description="Datetime format used for parsing")


class StringColumn(_BaseColumn):
    pass


class StructuredDataSet(_BaseDataSet):
    rowCount: int = Field(
        description="Number of row",
    )
    columnCount: int = Field(
        description="Number of columns",
    )
    numericColumnCount: int = Field(description="Numeric column count")
    datetimeColumnCount: int = Field(description="Datetime column count")
    stringColumnCount: int = Field(description="String column count")

    correlationGraph: Optional[FileReference] = Field(
        default=None, description="Reference to a correlation graph of the data columns"
    )
    numericColumns: List[NumericColumn] = Field(description="Numeric columns in this dataset")
    datetimeColumns: List[DateTimeColumn] = Field(description="Datetime columns in this dataset")
    stringColumns: List[StringColumn] = Field(
        description="Columns that could only be interpreted as string by the analysis"
    )
    primaryDatetimeColumn: Optional[str] = Field(
        default=None, description="Name of the datetime column that was determined to be the primary one."
    )

    @property
    def all_columns(self) -> Iterator[_BaseColumn]:
        yield from self.numericColumns
        yield from self.datetimeColumns
        yield from self.stringColumns

    def get_columns_dict(self) -> Dict[str, _BaseColumn]:
        return {column.name: column for column in self.all_columns}


class ImageColorMode(str, Enum):
    BLACK_AND_WHITE = "1"
    GRAYSCALE = "L"
    PALETTED = "P"
    RGB = "RGB"
    RGBA = "RGBA"
    CMYK = "CMYK"
    YCBCR = "YCbCr"
    LAB = "LAB"
    HSV = "HSV"
    INTEGER = "I"
    FLOAT = "F"


class ImageDimensions(BaseModel):
    width: int = Field(ge=0, description="Width of the image in pixels")
    height: int = Field(ge=0, description="Height of the image in pixels")


class ImageDPI(BaseModel):
    x: float = Field(ge=0.0, description="Dots Per Inch (DPI) along the x-axis")
    y: float = Field(ge=0.0, description="Dots Per Inch (DPI) along the y-axis")


class ImageDataSet(_BaseDataSet):
    codec: str = Field(description="The format codec of the image, such as JPEG or PNG")
    colorMode: ImageColorMode = Field(description="Color mode of the image, such as RGB, CMYK, Grayscale, etc.")
    resolution: ImageDimensions = Field(description="Dimensions of the image in pixels")
    dpi: ImageDPI = Field(description="Dots Per Inch (DPI) represents the image's print resolution")
    brightness: Optional[float] = Field(
        ge=0.0, le=255.0, description="Average brightness of the image, higher values indicate brighter images"
    )
    blurriness: Optional[float] = Field(
        ge=0.0, description="Measure of the image blurriness, with higher values indicating more blur"
    )
    sharpness: Optional[float] = Field(
        ge=0.0, le=100.0, description="Measure of the image sharpness, indicating the clarity of detail"
    )
    brisque: Optional[float] = Field(
        ge=0.0,
        description="No-reference metric for assessing perceived quality of an image, with lower scores typically indicating better quality",
    )
    noise: Optional[float] = Field(
        ge=0.0, description="Estimated absolute level of random variations (noise) in the image pixel intensities"
    )
    lowContrast: Optional[bool] = Field(description="Boolean indicator of whether the image is low contrast")


class ModificationState(str, Enum):
    modified = "modified"
    unmodified = "unmodified"
    unknown = "unknown"


class DocumentDataSet(_BaseDataSet):
    """Document dataset. Used for PDF and other formats.
    Spec for PDF metadata fields: https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/pdfreference1.7old.pdf#page=843
    """

    fileSize: int = Field(description="Size of the original document")
    title: Optional[str] = Field(description="The document's title")
    subject: Optional[str] = Field(description="The subject of the document")
    author: Optional[str] = Field(description="The name of the person who created the document")
    toolchain: Optional[str] = Field(
        description="The name of the application that created the original document or converted it"
    )
    creationDate: Optional[datetime] = Field(description="The date and time the document was created")
    modificationDate: Optional[datetime] = Field(
        description="The date and time the document was most recently modified"
    )
    keywords: List[str] = Field(description="Keywords associated with the document")
    docType: str = Field(description="Document type, e.g. PDF-1.6")
    numPages: int = Field(description="Number of pages in the document")
    numImages: int = Field(description="Number of images in the document")
    modified: ModificationState = Field(description="Modified from original version?")
    encrypted: bool = Field(description="Encrypted")


DataSet = Union[StructuredDataSet, ImageDataSet, DocumentDataSet]


class Publisher(BaseModel):
    name: str = Field(description="Name of the publisher")
    url: Optional[str] = Field(default=None, description="URL to the publisher")


class License(BaseModel):
    name: Optional[str] = Field(default=None, description="Name of the license")
    url: Optional[str] = Field(default=None, description="URL describing the license")


def validate_license(license: License):
    if license.name is None and license.url is None:
        raise ValueError("License model needs at least 'name' or 'url'")
    return license


class UserProvidedEdpData(BaseModel):
    """The part of the EDP dataset that can not be automatically generated, but needs to be provided by the user."""

    assetId: str = Field(description="The asset ID is a unique identifier for an asset within a data room")
    name: str = Field(description="Name of the asset")
    url: str = Field(description="The URL via which the asset can be found in the published data room")
    dataCategory: Optional[str] = Field(
        default=None,
        description="A data room-specific categorization of the asset (e.g. https://github.com/Mobility-Data-Space/mobility-data-space/wiki/MDS-Ontology",
    )
    dataSpace: DataSpace = Field(description="Dataspace the asset can be found")
    publisher: Publisher = Field(description="Provider that placed the asset in the data room")
    publishDate: datetime = Field(description="Date on which this asset has been published")
    license: Annotated[License, AfterValidator(validate_license)] = Field(
        description="Describes the data license under which the asset is made available by the data provider (see also https://www.dcat-ap.de/def/licenses/)"
    )
    assetProcessingStatus: Optional[AssetProcessingStatus] = Field(
        default=AssetProcessingStatus.original_data, description="Processing status of the asset"
    )
    description: Optional[str] = Field(default=None, description="Description of the asset")
    tags: List[str] = Field(default_factory=list, description="Optional list of tags")
    dataSubCategory: Optional[str] = Field(
        default=None, description="A data room-specific sub-categorization for assetDataCategory"
    )
    version: Optional[str] = Field(default=None, description="Provide supplied version of the asset")
    transferTypeFlag: Optional[DataSetTransfer] = Field(
        default=None, description="Describes whether an asset grows steadily over time "
    )
    immutabilityFlag: Optional[DataSetImmutability] = Field(default=None, description="Is the dataset immutable")
    growthFlag: Optional[DataSetVolume] = Field(
        default=None,
        description="If transfer is frequent, this parameter gives the growth rate of the dataset per day",
    )
    transferTypeFrequency: Optional[DataSetFrequency] = Field(
        default=None,
        description="If transfer is frequent, this parameter gives the update frequency",
    )
    nda: Optional[str] = Field(
        default=None, description="Identifier that describes or links to the non disclosure agreement"
    )
    dpa: Optional[str] = Field(default=None, description="Identifier that describes or links a dpa")
    dataLog: Optional[str] = Field(default=None, description="Description or links to data log")
    freely_available: bool = Field(
        description="Whether asset is freely available. That means, there is no registration or login needed to download it."
    )


class Config(BaseModel):
    userProvidedEdpData: UserProvidedEdpData = Field(description="User provided EDP meta data")
    augmentedColumns: List[AugmentedColumn] = Field(default_factory=list, description="List of augmented columns")


class Compression(BaseModel):
    algorithms: Set[str] = Field(description="List of all used compression algorithms in an asset")
    extractedSize: int = Field(description="Size in bytes when all compressions got extracted")


class ComputedEdpData(BaseModel):
    volume: int = Field(description="Volume of the asset in bytes")
    compression: Optional[Compression] = Field(default=None, description="Description of compressions used")
    dataTypes: Set[DataSetType] = Field(description="Types of data contained in this asset")
    temporalCover: Optional[TemporalCover] = Field(
        default=None, description="Earliest and latest dates contained in this asset"
    )
    periodicity: Optional[str] = Field(
        default=None,
        description="The periodicity of the index date time field of the first structured dataset",
    )

    structuredDatasets: List[StructuredDataSet] = Field(
        default_factory=list,
        description="Metadata for all datasets (files) detected to be structured (tables)",
    )
    imageDatasets: List[ImageDataSet] = Field(
        default_factory=list,
        description="Metadata for all datasets detected to be images",
    )
    documentDatasets: List[DocumentDataSet] = Field(
        default_factory=list,
        description="Metadata for all datasets detected to be documents",
    )


class ExtendedDatasetProfile(UserProvidedEdpData, ComputedEdpData):
    schema_version: Literal[SchemaVersion.V0] = Field(
        default=SchemaVersion.V0, description="Version of the JSON Schema used to generate this EDP"
    )
