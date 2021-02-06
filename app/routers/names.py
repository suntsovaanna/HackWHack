from fastapi import APIRouter
from typing import List
from pydantic import BaseModel

router = APIRouter()


class NameQuery(BaseModel):
    fullName: str


class BulkNameQuery(BaseModel):
    fullNames: List[str]


@router.post('/name')
async def parse_name(data: NameQuery):
    return data.fullName


@router.post('/names')
async def parse_name_array(data: BulkNameQuery):
    return data.fullNames[0]