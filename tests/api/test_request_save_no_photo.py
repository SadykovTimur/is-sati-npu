import allure
from _pytest.fixtures import FixtureRequest

from tests.api.steps import save_no_photo


@allure.epic('IS-SATI-NPU')
@allure.title('Отправить запрос на сохранение фото без фото')
def test_request_save_no_photo(request: FixtureRequest) -> None:
    save_no_photo(request)
