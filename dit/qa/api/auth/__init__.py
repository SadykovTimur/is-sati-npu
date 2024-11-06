import json
import os
from typing import Any, Tuple

import requests
from _pytest.fixtures import FixtureRequest

from tests.api.constants import token


def auth(request: FixtureRequest) -> Tuple[int, Any]:
    headers = {
        "Authorization": f'Bearer {token}',
    }

    response = requests.get(
        f'{request.config.option.api_url}/identcheck',
        headers=headers,
        timeout=25,
    )
    result = json.loads(response.text)

    return response.status_code, result


def device_status(request: FixtureRequest) -> Tuple[int, Any]:
    headers = {
        "Authorization": f'Bearer {token}',
    }

    response = requests.get(
        f'{request.config.option.api_url}/status',
        headers=headers,
        timeout=20,
    )
    result = json.loads(response.text)

    return response.status_code, result


def request_photo(request: FixtureRequest, photo: bool = False) -> Tuple[int, Any]:
    headers = {
        "Authorization": f'Bearer {token}',
    }
    if photo:
        with open('img.png', 'rb') as file:
            data = file.read()
    else:
        data = None

    response = requests.post(
        f'{request.config.option.api_url}/photo',
        headers=headers,
        timeout=20,
        files={"photo": data},
    )
    result = json.loads(response.text)

    return response.status_code, result


def request_message_server(request: FixtureRequest) -> Tuple[int, Any]:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}',
    }

    data_raw = [
        {
            "accuracy": 24,
            "altitude": 240.2,
            "os_version": "Android 10",
            "battery_level": 76,
            "bearing": 0,
            "charge": 'false',
            "datetime": "2021-01-30T13:47:03",
            "device_model": "SAMSUNG SM-G970F",
            "device_screen_height": 2280,
            "device_screen_width": 1080,
            "install_datetime": "2021-01-30T11:20:59Z",
            "locationDatetime": "2021-01-30T15:17:02",
            "lat": 55.8656457,
            "lon": 37.4939842,
            "locationStatus": {"gps": 'true', "isPermissionGranted": 'true', "network": 'true', "passive": 'true'},
            "provider": "fused",
            "speed": 0.0,
            "step_count": -1,
            "version": 111,
            "version_ext": "1.11 (1526)",
        }
    ]

    response = requests.post(
        f'{request.config.option.api_url}/message',
        headers=headers,
        timeout=20,
        json=data_raw,
    )
    result = json.loads(response.text)

    return response.status_code, result
