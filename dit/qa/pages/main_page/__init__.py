from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

__all__ = ['MainPage']


class MainPage(Page):
    nav = Component(tag="nav")
    folder = Button(css='[class*="tab__trigger"]')
    patient = Button(xpath='//div[contains(text(),"Пациенты ФМ")]')
    fm_monitoring = Component(xpath='//div[text()="ФМ Мониторинг"]')
    dit = Button(xpath='//div[text()=" ДИТ "]')
    report = Button(xpath='//div[text()=" 02. Отчеты "]')
    required_monitoring = Button(css='[title="Требуется мониторинг"]')
    not_required_monitoring = Button(css='[title="Мониторинг не требуется"]')
    func_monitoring = Button(xpath='//div[text()=" 08. Функциональный мониторинг "]')
    check_monitoring = Button(xpath='//div[text()=" Требуется мониторинг "]')
    uncheck_monitoring = Button(xpath='//div[text()=" Мониторинг не требуется "]')
    status_monitoring = Button(xpath='//div[text()="Статус мониторинга:"]')
    home = Component(css='[class*="custom_home"]')
    user = Button(class_name='sidebar__user')
    logout = Button(xpath='//button[text()="Выйти"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.home.visible
                assert self.folder.visible
                assert self.user.visible

                return self.nav.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Главная страница не отображена')
        self.app.restore_implicitly_wait()

    def wait_patient(self) -> None:
        def condition() -> bool:
            try:
                return self.patient.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Отчет "Пациенты ФМ" не отображен')
        self.app.restore_implicitly_wait()

    def wait_report_patient(self) -> None:
        def condition() -> bool:
            try:
                return self.fm_monitoring.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Отчет "Пациенты ФМ" не открыт')
        self.app.restore_implicitly_wait()

    def wait_status_monitoring(self) -> None:
        def condition() -> bool:
            try:
                assert self.check_monitoring.visible

                return self.uncheck_monitoring.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Выпадающий список не доступен')
        self.app.restore_implicitly_wait()

    def wait_data_filter(self) -> None:
        def condition() -> bool:
            try:
                return not self.fm_monitoring.visible

            except NoSuchElementException:

                return True

        self.app.set_implicitly_wait(1)
        wait_for(
            condition,
            msg='Запись из таблицы у которой в атрибуте "Статус мониторинг" значение "Требуется '
            'мониторинг" не пропала',
        )
        self.app.restore_implicitly_wait()

    def wait_change_reference_data(self) -> None:
        def condition() -> bool:
            try:
                return self.not_required_monitoring.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Выбранное значение в атрибуте "Статус мониторинга" не сохранилось')
        self.app.restore_implicitly_wait()
