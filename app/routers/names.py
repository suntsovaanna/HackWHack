from fastapi import APIRouter, Depends
from typing import List
from pydantic import BaseModel
from functools import lru_cache
from recognizer.recognition import NameRecognizer
from recognizer.grammars import name_parser


router = APIRouter()


class NameQuery(BaseModel):
    fullName: str


@lru_cache()
def get_named_parser():
    return NameRecognizer(name_parser)


NAME_RECOGNIZER = Depends(get_named_parser)


@router.post('/name')
def parse_name(data: NameQuery, name_recognizer: NameRecognizer = NAME_RECOGNIZER):
    return name_recognizer(data.fullName)


@router.post('/names')
async def parse_name_array(data: List[NameQuery]):
    return [parse_name(name) for name in data]
