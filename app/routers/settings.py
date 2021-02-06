from fastapi import APIRouter
from pydantic import BaseSettings


class SettingsModel(BaseSettings):
    shouldFixCasing: bool = False
    normalizeFirstName: bool = False
    spellCheckEnabled: bool = False
    verbose: bool = False


router = APIRouter()
defaultSettings = SettingsModel()
settings = SettingsModel()

@router.get('/settings')
async def get_settings():
    return settings


@router.post('/settings')
async def update_settings(data: SettingsModel):
    global settings
    settings = data


@router.delete('/settings')
async def reset_settings():
    global settings
    settings = defaultSettings
