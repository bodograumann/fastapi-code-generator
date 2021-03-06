# generated by datamodel-codegen:
#   filename:  simple.yaml
#   timestamp: 2020-06-19T00:00:00+00:00

from typing import List, Optional

from pydantic import BaseModel


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None


class Pets(BaseModel):
    __root__: List[Pet]


class Error(BaseModel):
    code: int
    message: str
