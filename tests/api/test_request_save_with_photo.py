import allure
from _pytest.fixtures import FixtureRequest

from tests.api.steps import save_with_photo


@allure.epic('IS-SATI-NPU')
@allure.title('Отправить запрос на сохранение фото с фото')
def test_request_save_with_photo(request: FixtureRequest) -> None:
    save_with_photo(request, True)
