from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Menu']


class MenuWrapper(ComponentWrapper):
    user = Component(xpath='//span[text()="DIT D. D."]')
    directory = Button(xpath='//span[text()="Справочники"]')
    data_base = Button(xpath='//span[text()="База данных"]')
    documents = Component(xpath='//span[text()="Шаблоны документов"]')
    messages = Component(xpath='//span[text()="Обмен сообщениями"]')

    @property
    def is_visible(self) -> bool:
        assert self.user.visible
        assert self.directory.visible
        assert self.data_base.visible
        assert self.documents.visible

        return self.messages.visible


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
