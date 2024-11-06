import allure
from _pytest.fixtures import FixtureRequest

from tests.api.steps import transferring_identification_mobile_device


@allure.epic('IS-SATI-NPU')
@allure.title('Передача информации о запросе идентификации на мобильное устройство')
def test_identification_mobile_device(request: FixtureRequest) -> None:
    transferring_identification_mobile_device(request)
