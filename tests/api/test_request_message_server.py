import allure
from _pytest.fixtures import FixtureRequest

from tests.api.steps import request_message


@allure.epic('IS-SATI-NPU')
@allure.title('Отправка сообщения с устройства на сервер')
def test_request_message_server(request: FixtureRequest) -> None:
    request_message(request)
