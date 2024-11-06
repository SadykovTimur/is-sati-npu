import allure
from _pytest.fixtures import FixtureRequest

from dit.qa.api.auth import auth, device_status, request_message_server, request_photo

__all__ = [
    'transferring_identification_mobile_device',
    'request_device',
    'request_message',
    'save_no_photo',
    'save_with_photo',
]


def transferring_identification_mobile_device(request: FixtureRequest) -> None:
    with allure.step('Transferring identification mobile device'):
        code, response = auth(request)

        assert code == 200, f"Код ответа {code} не соответствует ожидаемому"
        assert (
            response['message']
            == 'Ожидайте уведомление о необходимости отправить фотографию в приложении и СМС-сообщении'
        )


def request_device(request: FixtureRequest) -> None:
    with allure.step('Request device_status'):
        code, response = device_status(request)

        assert code == 200, f"Код ответа {code} не соответствует ожидаемому"
        assert response['status'] == 'active'


def request_message(request: FixtureRequest) -> None:
    with allure.step('Request message'):
        code, response = request_message_server(request)

        assert code == 200, f"Код ответа {code} не соответствует ожидаемому"
        assert response[0]['message_update'] == 3


def save_no_photo(request: FixtureRequest, photo: bool = False) -> None:
    with allure.step('Saving no photo'):
        code, response = request_photo(request, photo)

        assert code == 400, f"Код ответа {code} не соответствует ожидаемому"
        assert response['message'] == 'Не передан файл'


def save_with_photo(request: FixtureRequest, photo: bool = True) -> None:
    with allure.step('Saving with photo'):
        code, response = request_photo(request, photo)

        assert code == 200, f"Код ответа {code} не соответствует ожидаемому"
        assert response['code'] == 200
