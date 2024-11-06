import allure
from _pytest.fixtures import FixtureRequest

from tests.api.steps import request_device


@allure.epic('IS-SATI-NPU')
@allure.title('Запрос статуса устройства')
def test_request_device_status(request: FixtureRequest) -> None:
    request_device(request)
