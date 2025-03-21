from datetime import datetime, timedelta
from enum import Enum
from pathlib import PurePosixPath
from typing import Any, Dict, Iterator, List, Optional, Set, Tuple, Union

from packaging.version import InvalidVersion, Version
from pydantic import (
    AnyUrl,
    BaseModel,
    Field,
    field_validator,
    model_validator,
)

from extended_dataset_profile.models.v0.json_reference import JsonReference
from extended_dataset_profile.models.v0.languages import Language
from extended_dataset_profile.version import CURRENT_VERSION


class AssetProcessingStatus(str, Enum):
    """Marks what kind of data an asset contains.

    The rough order of operations is:
    Original Data -> Processed Data -> Refined Data -> AI/ML Result Data.
    """

    original_data = "Original Data"
    processed_data = "Processed Data"
    refined_data = "Refined Data"
    ai_ml_result_data = "AI/ML Result Data"


class AssetTransferType(str, Enum):
    """Whether an asset was statically uploaded once or gets updated/inflated on a regular basis."""

    static = "static"
    frequent = "inflationary"


class AssetGrowthRate(str, Enum):
    """Rate at which an asset grows."""

    b_d = "Bytes/day"
    kb_d = "KiloBytes/day"
    mb_d = "MegaBytes/day"
    gb_d = "GigaBytes/day"
    tb_d = "TeraBytes/day"
    pb_d = "PetaBytes/day"


class AssetUpdatePeriod(str, Enum):
    """Describes how often an asset is updated"""

    static = "static"
    second = "updates by second"
    minute = "updates by minute"
    hour = "updates by hour"
    day = "updates by day"


class AssetImmutability(str, Enum):
    """Whether the data set can be modified in the given data spaces"""

    immutable = "immutable"
    not_immutable = "not-immutable"


class DataSetType(str, Enum):
    archive = "archive"
    structured = "structured"
    semiStructured = "semiStructured"
    unstructuredText = "unstructuredText"
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


class FileProperties(BaseModel):
    name: str = Field(description="Original file name")
    fileType: str = Field(description="File type")
    size: int = Field(description="Size of the file in bytes.")


class DatasetTreeNode(BaseModel):
    dataset: JsonReference = Field(description="Reference to the dataset this node refers to.")
    parent: Optional[JsonReference] = Field(
        default=None, description="Reference to the dataset tree node of the parent dataset, if any"
    )
    name: str = Field(description="Name of the dataset")
    fileProperties: Optional[FileProperties] = Field(
        description="File specific properties, if this dataset is a file. Otherwise none."
    )


class ArchiveDataSet(BaseModel):
    """Dataset representing an archive."""

    algorithm: str = Field(description="Compression algorithm used by this archive.")
    extractedSize: int = Field(
        description="Size in bytes when the archive is extracted. Does not include recursive archives."
    )


class Augmentation(BaseModel):
    """Information about how a column of a dataset has been augmented or created."""

    sourceColumns: List[str] = Field(description="List of source columns on which the augmented column is based")
    formula: Optional[str] = Field(
        default=None,
        description="The calculation that was applied to the source columns to create the augmented column",
    )
    parameters: List[str] = Field(default_factory=list, description="The parameters used for the calculation")


class _BaseColumn(BaseModel):
    name: str = Field(description="Name of the column")
    nullCount: int = Field(
        description="Number of empty and null entries in the column. Does not include the count of inconsistent entries."
    )
    inconsistentCount: int = Field(
        description="Number of entries which are inconsistent with the determined data type of this column."
    )
    interpretableCount: int = Field(
        description="Number of entries which are not empty and could be converted to the determined type of this column."
    )
    numberUnique: int = Field(description="Number of unique values.")
    augmentation: Optional[Augmentation] = Field(
        default=None, description="If this column was augmented this filed contains all relevant information"
    )


class TimeBasedGraph(BaseModel):
    timeBaseColumn: str
    file: FileReference


class NumericColumn(_BaseColumn):
    min: Numeric = Field(description="Minimum value that occurred in this column")
    max: Numeric = Field(description="Maximum value that occurred in this column")
    mean: Numeric = Field(description="Mean of all values in this column")
    median: Numeric = Field(description="Median of all values in this column")
    variance: Numeric = Field(description="Statistical variance of this column")
    stddev: Numeric = Field(description="Statistical standard deviation of this column")
    upperPercentile: Numeric = Field(description="Value of the upper 1% quantile")
    lowerPercentile: Numeric = Field(description="Value of the lower 1% quantile")
    percentileOutlierCount: int = Field(description="Number of elements in the lower or upper percentile")
    upperQuantile: Numeric = Field(description="Value of the upper 25% quantile")
    lowerQuantile: Numeric = Field(description="Value of the lower 25% quantile")
    quantileOutlierCount: int = Field(description="Number of elements in the lower or upper quantile")
    upperZScore: Numeric = Field(description="Value of the upper standard score")
    lowerZScore: Numeric = Field(description="Value of the lower standard score")
    zScoreOutlierCount: int = Field(description="Number of elements outside the lower and upper standard scores")
    upperIQR: Numeric = Field(description="Value of the upper limit of the inter quartile range (25%)")
    lowerIQR: Numeric = Field(description="Value of the lower limit of the inter quartile range (25%)")
    iqr: Numeric = Field(description="Value of the inter quartile range")
    iqrOutlierCount: int = Field(description="Number of elements outside of the inter quartile range")
    relativeOutlierCount: float = Field(
        description="Averages all outlier counts into a relative outlier measure [0.0, 1.0].", ge=0.0, le=1.0
    )
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
    dataType: str = Field(
        description="More specific type the data in this column can be represented at without loosing information"
    )


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
    distributionGraph: Optional[FileReference] = Field(
        description="Graph of the distribution of string values, if enough unique values where present."
    )


class CorrelationSummary(BaseModel):
    no: int = Field(default=0, description="Count of column pairs with no correlation")
    partial: int = Field(default=0, description="Count of column pairs with partial correlation")
    strong: int = Field(default=0, description="Count of column pairs with strong correlation")


class StructuredDataSet(BaseModel):
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
    correlationSummary: CorrelationSummary = Field(description="Mapping from correlation level to count of occurrences")
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


class SemiStructuredDataSet(BaseModel):
    jsonSchema: str = Field(description="JSON schema of the semi-structured data")


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


class Resolution(BaseModel):
    width: int = Field(ge=0, description="Width in pixels")
    height: int = Field(ge=0, description="Height in pixels")


class ImageDPI(BaseModel):
    x: float = Field(ge=0.0, description="Dots Per Inch (DPI) along the x-axis")
    y: float = Field(ge=0.0, description="Dots Per Inch (DPI) along the y-axis")


class ImageDataSet(BaseModel):
    codec: str = Field(description="The format codec of the image, such as JPEG or PNG")
    colorMode: ImageColorMode = Field(description="Color mode of the image, such as RGB, CMYK, Grayscale, etc.")
    resolution: Resolution = Field(description="Dimensions of the image in pixels")
    dpi: ImageDPI = Field(description="Dots Per Inch (DPI) represents the image's print resolution")
    brightness: Optional[float] = Field(
        ge=0.0, le=255.0, description="Average brightness of the image, higher values indicate brighter images"
    )
    blurriness: Optional[float] = Field(
        ge=0.0, description="Measure of the image blurriness, with higher values indicating more blur"
    )
    sharpness: Optional[float] = Field(
        ge=0.0, description="Measure of the image sharpness, indicating the clarity of detail"
    )
    brisque: Optional[float] = Field(
        ge=0.0,
        description="No-reference metric for assessing perceived quality of an image, with lower scores typically indicating better quality",
    )
    noise: Optional[float] = Field(
        ge=0.0, description="Estimated absolute level of random variations (noise) in the image pixel intensities"
    )
    lowContrast: Optional[bool] = Field(description="Boolean indicator of whether the image is low contrast")
    elaScore: Optional[float] = Field(
        ge=0.0,
        description="Computed Error Level Analysis (ELA) score: the average pixel intensity difference between the original image and its recompressed version",
    )


class VideoCodec(Enum):
    H264 = "h264"
    HEVC = "hevc"
    MPEG4 = "mpeg4"
    VP9 = "vp9"
    AV1 = "av1"
    PRORES = "prores"
    DNXHD = "dnxhd"
    H263 = "h263"
    FLV1 = "flv1"
    WMV2 = "wmv2"
    UNKNOWN = "unknown"


class VideoPixelFormat(Enum):
    YUV420P = "yuv420p"
    YUV422P = "yuv422p"
    YUV444P = "yuv444p"
    NV12 = "nv12"
    GRAY = "gray"
    RGB24 = "rgb24"
    BGR24 = "bgr24"
    YUVJ420P = "yuvj420p"
    YUVJ422P = "yuvj422p"
    YUVJ444P = "yuvj444p"
    UNKNOWN = "unknown"


class VideoDataSet(BaseModel):
    codec: VideoCodec = Field(description="The format codec of the video, such as H264 or HEVC")
    resolution: Resolution = Field(description="Dimensions of the video in pixels")
    fps: float = Field(description="Frames per second of the video")
    duration: float = Field(description="Duration of the video in seconds")
    pixel_format: VideoPixelFormat = Field(description="Pixel format of the video")


class ModificationState(str, Enum):
    modified = "modified"
    unmodified = "unmodified"
    unknown = "unknown"


class DocumentDataSet(BaseModel):
    """Document dataset. Used for PDF and other formats.
    Spec for PDF metadata fields: https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/pdfreference1.7old.pdf#page=843
    """

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
    numPages: Optional[int] = Field(description="Number of pages in the document")
    numImages: int = Field(description="Number of images in the document")
    modified: ModificationState = Field(description="Modified from original version?")
    encrypted: bool = Field(description="Encrypted")


class Chunk(BaseModel):
    """Chunk of text identified by its start and end lines. The indices are 0-based."""

    startLine: int = Field(description="Inclusive start line index.")
    endLine: int = Field(description="Exclusive end line index.")

    @model_validator(mode="after")
    def _end_after_start(self):
        if self.endLine <= self.startLine:
            raise RuntimeError("End line index must be larger than start line index!")
        return self

    def __len__(self) -> int:
        return self.endLine - self.startLine


class EmbeddedTable(Chunk):
    structuredDatasetName: str = Field(
        description="Name of the structured dataset this embedded dataset got analyzed as."
    )


class UnstructuredTextDataSet(BaseModel):
    embeddedTables: List[EmbeddedTable] = Field(
        default_factory=list, description="Chunks that are identified to contain tables."
    )
    languages: Set[Language] = Field(description="Set of ISO639-3 languages identifiers detected in the text.")
    wordCloud: List[Tuple[str, int]] = Field(
        default_factory=list,
        description="List of (word, frequency) pairs representing the most frequently occurring words in the text.",
    )
    lineCount: int = Field(description="Number of lines (excluding embedded tables) inside the text block.")
    wordCount: int = Field(description="Number of words (excluding embedded tables) inside the text block.")


class Publisher(BaseModel):
    """The entity that uploaded a data set / asset"""

    name: str = Field(description="Name of the publisher")
    url: Optional[str] = Field(default=None, description="URL to the publisher")


class License(BaseModel):
    """A license of some sort. Can contain a name and URL, but must specify at least one."""

    name: Optional[str] = Field(default=None, description="Name of the license")
    url: Optional[str] = Field(default=None, description="URL describing the license")

    @model_validator(mode="after")
    def validate_license(self) -> "License":
        if self.name is None and self.url is None:
            raise ValueError("License model needs at least 'name' or 'url'")
        return self


class DataSpace(BaseModel):
    """Represents a data space."""

    name: str = Field(description="Name of the data space")
    url: str = Field(description="URL of the data space")


class AssetReference(BaseModel):
    """Reference to a dataset in a data space."""

    assetId: str = Field(description="Unique identifier for an asset within the data space")
    assetUrl: AnyUrl = Field(description="URL where the asset can be found in the published data space")
    assetVersion: Optional[str] = Field(default=None, description="Provide supplied version of the asset")
    dataSpace: DataSpace = Field(description="Data space the asset can be found in")
    publisher: Publisher = Field(description="Provider that placed the asset in the data room")
    publishDate: datetime = Field(description="Date on which this asset has been published")
    license: License = Field(
        description="Describes the data license under which the asset is made available by the data provider (see also https://www.dcat-ap.de/def/licenses/)"
    )


class ExtendedDatasetProfile(BaseModel):
    schemaVersion: str = Field(
        default=str(CURRENT_VERSION),
        validation_alias="schema_version",
        description="Version of the JSON Schema used to generate this EDP",
    )
    name: str = Field(description="Name of the asset")
    assetRefs: List[AssetReference] = Field(
        min_length=1,
        default_factory=list,
        description="References to multiple dataspace locations for the asset",
    )
    dataCategory: Optional[str] = Field(
        default=None,
        description="A data room-specific categorization of the asset (e.g. https://github.com/Mobility-Data-Space/mobility-data-space/wiki/MDS-Ontology",
    )
    assetProcessingStatus: Optional[AssetProcessingStatus] = Field(
        default=AssetProcessingStatus.original_data, description="Processing status of the asset"
    )
    description: Optional[str] = Field(default=None, description="Description of the asset")
    tags: List[str] = Field(default_factory=list, description="Optional list of tags")
    dataSubCategory: Optional[str] = Field(
        default=None, description="A data room-specific sub-categorization for assetDataCategory"
    )
    assetTypeInfo: Optional[str] = Field(default=None, description="Additional type-specific information for the asset")
    generatedBy: str = Field(
        description="Name and version of the toolchain that generated this extended dataset profile"
    )
    transferTypeFlag: Optional[AssetTransferType] = Field(
        default=None, description="Describes whether an asset grows steadily over time."
    )
    transferTypeFrequency: Optional[AssetUpdatePeriod] = Field(
        default=None, description="Describes how often a data set is updated."
    )
    growthFlag: Optional[AssetGrowthRate] = Field(
        default=None,
        description="Growth rate of the dataset per day",
    )
    immutabilityFlag: Optional[AssetImmutability] = Field(default=None, description="Is the dataset immutable")
    nda: Optional[str] = Field(
        default=None, description="Identifier that describes or links to the non disclosure agreement"
    )
    dpa: Optional[str] = Field(default=None, description="Identifier that describes or links a dpa")
    dataLog: Optional[str] = Field(default=None, description="Description or links to data log")
    freely_available: bool = Field(
        description="Whether asset is freely available. That means, there is no registration or login needed to download it."
    )

    volume: int = Field(description="Volume of the asset in bytes")
    dataTypes: Set[DataSetType] = Field(default_factory=set, description="Types of data contained in this asset")
    temporalCover: Optional[TemporalCover] = Field(
        default=None, description="Earliest and latest dates contained in this asset"
    )
    periodicity: Optional[str] = Field(
        default=None,
        description="The periodicity of the index date time field of the first structured dataset",
    )
    assetSha256Hash: str = Field(description="Cryptographic sha-256 hash of the asset")

    archiveDatasets: List[ArchiveDataSet] = Field(
        default_factory=list, description="Metadata for all archives detected"
    )
    structuredDatasets: List[StructuredDataSet] = Field(
        default_factory=list,
        description="Metadata for all datasets detected to be structured (tables)",
    )
    semiStructuredDatasets: List[SemiStructuredDataSet] = Field(
        default_factory=list, description="Metadata for all datasets detected to be semi-structured"
    )
    unstructuredTextDatasets: List[UnstructuredTextDataSet] = Field(
        default_factory=list, description="Metadata for all datasets detected to be unstructured text (e.g. txt files)"
    )
    imageDatasets: List[ImageDataSet] = Field(
        default_factory=list,
        description="Metadata for all datasets detected to be images",
    )
    videoDatasets: List[VideoDataSet] = Field(
        default_factory=list,
        description="Metadata for all datasets detected to be videos",
    )
    documentDatasets: List[DocumentDataSet] = Field(
        default_factory=list,
        description="Metadata for all datasets detected to be documents",
    )

    datasetTree: List[DatasetTreeNode] = Field(
        default_factory=list,
        description="List of tree nodes that describe the hierarchy of the datasets contained in this extended dataset profile.",
    )

    @field_validator("schemaVersion", mode="before")
    @classmethod
    def parse_version(cls, value: Any) -> str:
        if isinstance(value, str):
            try:
                MAJOR_VERSION = 0
                version = Version(value)
                if MAJOR_VERSION != version.major:
                    raise ValueError(f"schemaVersion {value} does not match expected major version '{MAJOR_VERSION}'")
                return value
            except InvalidVersion:
                raise ValueError(f"Invalid schema version '{value}'")
        raise ValueError(f"Invalid schema version '{value}'")
