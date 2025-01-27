from argparse import ArgumentParser
from pathlib import Path
from typing import Any, Dict, Type

from pydantic import BaseModel, TypeAdapter


def export_schema(schema: Type[BaseModel]):
    args = _get_args()
    output: Path = args.output
    if output.is_dir():
        output /= "edp_schema.json"
    adapter = TypeAdapter(Dict[str, Any])
    with open(output, "wb") as file:
        file.write(adapter.dump_json(schema.model_json_schema()))


def _get_args():
    parser = ArgumentParser()
    parser.add_argument("-o", "--output", type=Path, required=True, help="PurePosixPath to output the schema to")
    return parser.parse_args()
