import datetime


class HistoryItem:
    def __init__(self, url, datetime):
        """
        Формирует ноду
        :param url:
        :param datetime:
        """
        self.url = url
        self.timestamp = datetime
        self.prev = None


class BrowserHistory:
    def __init__(self):
        self.__history_stack = []
        self.__current_index = 0
        self.__top = None

    def visit(self, url) -> bool:
        """
         Создает новый объект HistoryItem с текущим временем и добавляет его в стек. Обрезает историю впереди,
         Если пользователь возвращался назад и выбрал новый URL.
        :param url: Пренимает адрес страницы
        :return: str
        """
        node = HistoryItem(url, datetime)

        if 'http' not in node.url: return False

        self.__history_stack.append(node.url)

        if self.__current_index == 0:
            self.__top = node

        node.prev = self.__top
        self.__top = node

        self.__current_index += 1

        return True

    def back(self) -> str:
        """
        :return: Возвращает предыдущий объект HistoryItem в истории.
        """
        return self.__top.prev.url if self.__current_index > 1 else False

    def forward(self) -> str:
        """
        :return: Возвращает следующий объект HistoryItem в истории после предыдущего использования back()
        """
        return self.__top.url if self.__current_index > 0 else False

    def clear(self) -> bool:
        """
        Очищает всю историю просмотра страниц.
        :return: str
        """
        self.__top = None

        self.__current_index = 0

        self.__history_stack = []

        return True

    def all(self):
        """
        :return:  Возвращает всю историю просмотра страниц в формате одной форматированной строки.
        """
        all_site = ', '.join(self.__history_stack)
        return (f'Вся история просмотра страниц:\n{all_site}') if self.__current_index > 0 else False

    @staticmethod
    def validate_input_data(data):
        """
        Выполняет проверку полученных данных
        :return:
        """
        return True if data == 'visit' or data == 'back' or data == 'forward' or data == 'clear' or data == 'all' or data == 'exit' or data == 'info' else False

