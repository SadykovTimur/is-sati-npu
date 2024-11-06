import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from dit.qa.pages.main_page import MainPage
from dit.qa.pages.start_page import StartPage

__all__ = [
    'open_start_page',
    'sign_in',
    'open_main_page',
    'logout',
    'open_nav',
    'open_report_patient',
    'check_parameters',
    'change_data_filter_remove_checkbox',
    'change_data_filter_put_checkbox',
    'check_reference_data',
    'change_reference_data',
]


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()

            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = StartPage(app)

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Ошибка ввода данных') from e

        auth_form.submit.click()


def open_main_page(app: Application) -> None:
    with allure.step('Opening Main page'):
        try:
            MainPage(app).wait_for_loading()

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise e


def logout(app: Application) -> None:
    with allure.step('Logout'):
        try:
            page = MainPage(app)
            page.user.click()
            page.logout.click()

            StartPage(app).wait_for_loading()

            screenshot_attach(app, 'logout')
        except Exception as e:
            screenshot_attach(app, 'logout_error')

            raise e


def open_nav(app: Application) -> None:
    with allure.step('Opening nav'):
        try:
            page = MainPage(app)
            page.folder.click()
            page.dit.click()
            page.report.click()
            page.func_monitoring.click()

            page.wait_patient()

            screenshot_attach(app, 'nav')
        except Exception as e:
            screenshot_attach(app, 'nav_error')

            raise e


def open_report_patient(app: Application) -> None:
    with allure.step('Opening report patient'):
        try:
            page = MainPage(app)
            ActionChains(app.driver).double_click(page.patient.webelement).perform()  # type: ignore[no-untyped-call]

            page.wait_report_patient()

            screenshot_attach(app, 'report_patient')
        except Exception as e:
            screenshot_attach(app, 'report_patient_error')

            raise e


def check_parameters(app: Application) -> None:
    with allure.step('Checking parameters'):
        try:
            page = MainPage(app)
            page.status_monitoring.click()

            page.wait_status_monitoring()

            screenshot_attach(app, 'parameters')
        except Exception as e:
            screenshot_attach(app, 'parameters_error')

            raise e


def change_data_filter_remove_checkbox(app: Application) -> None:
    with allure.step('Changing data filter remove checkbox'):
        try:
            page = MainPage(app)
            page.check_monitoring.click()
            page.status_monitoring.click()

            page.wait_data_filter()

            screenshot_attach(app, 'data_filter_remove_checkbox')
        except Exception as e:
            screenshot_attach(app, 'data_filter_remove_checkbox_error')

            raise e


def change_data_filter_put_checkbox(app: Application) -> None:
    with allure.step('Changing data filter put checkbox'):
        try:
            page = MainPage(app)
            page.status_monitoring.click()
            page.check_monitoring.click()
            page.status_monitoring.click()

            page.wait_report_patient()

            screenshot_attach(app, 'data_filter_put_checkbox')
        except Exception as e:
            screenshot_attach(app, 'data_filter_put_checkbox_error')

            raise e


def check_reference_data(app: Application) -> None:
    with allure.step('Checking reference data'):
        try:
            page = MainPage(app)
            ActionChains(app.driver).double_click(  # type:ignore[no-untyped-call]
                page.required_monitoring.webelement
            ).perform()

            page.wait_status_monitoring()

            screenshot_attach(app, 'reference_data')
        except Exception as e:
            screenshot_attach(app, 'reference_data_error')

            raise e


def change_reference_data(app: Application) -> None:
    with allure.step('Changing reference data'):
        try:
            page = MainPage(app)
            page.uncheck_monitoring.click()

            page.wait_change_reference_data()

            screenshot_attach(app, 'reference_data')
        except Exception as e:
            screenshot_attach(app, 'reference_data_error')

            raise e
