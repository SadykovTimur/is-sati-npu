from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    change_data_filter_put_checkbox,
    change_data_filter_remove_checkbox,
    check_parameters,
    check_reference_data,
    open_main_page,
    open_nav,
    open_report_patient,
    open_start_page,
    sign_in,
)


@allure.epic('IS-SATI-NPU')
@allure.title('Получение справочных данных')
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_check_reference_data(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:
    app = make_app(browser, device_type)

    open_start_page(app)
    sign_in(app, request.config.option.username, request.config.option.password)

    open_main_page(app)

    open_nav(app)

    open_report_patient(app)

    check_parameters(app)

    change_data_filter_remove_checkbox(app)

    change_data_filter_put_checkbox(app)

    check_reference_data(app)
