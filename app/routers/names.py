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

# spell = SpellChecker(language=None, case_sensitive=False)
# spell.word_frequency.load_text_file('../data/first.txt')
# spell.word_frequency.load_text_file('../data/last.txt')


def correct(part: str):
    if part in spell:
        return part
    else:
        return correction(part)


@router.get('/check')
def correction(name: str):
    is_lower = name.islower()
    result = spell.correction(name)
    return result if is_lower else result.capitalize()


@router.post('/name')
def parse_name(data: NameQuery, name_recognizer: NameRecognizer = NAME_RECOGNIZER):
    # parts = data.fullName.split(sep=' ')
    # lower_parts = [correct(part) for part in parts]
    # joined = ' '.join(lower_parts)
    return name_recognizer(data.fullName)


@router.post('/names')
async def parse_name_array(data: List[NameQuery]):
    return [parse_name(name) for name in data]
