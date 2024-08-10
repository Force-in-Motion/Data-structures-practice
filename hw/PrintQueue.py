
class PrintDocument:
    def __init__(self, title, number_of_pages):
        self.title = title
        self.number_of_pages =  number_of_pages
        self.prev = None


class PrintQueue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, title, number_of_pages) -> bool:
        """
        Добавляет документ document в конец очереди
        :param title: Пренимает название докумениа
        :param number_of_pages: Пренимает номер страницы
        :return: bool
        """

        doc = PrintDocument(title, number_of_pages)

        if self.__count == 0:
            self.__head = doc
            self.__tail = doc
            return True

        self.__count += 1

        self.__tail.prev = doc
        self.__tail = doc

        return True

    def dequeue(self) -> bool or None:
        """
        Удаляет и возвращает первый документ из очереди. Если очередь пуста, возвращает None.
        :return: Если очередь пуста, возвращает None или первый документ из очереди если удаление успешно выполнено
        """
        assert self.__count != 0, ValueError('Очередь пуста, удалять нечего, для начала добавьте документы в нее')

        one_doc = self.__head

        self.__head = self.__head.prev

        self.__count -= 1

        return one_doc

    def __peek(self):
        """
        :return: Возвращает первый документ с головы очереди
        """
        return self.__head.title

    def __get_tail(self):
        """
        :return: Возвращает последний документ с хвоста очереди
        """
        return self.__tail.title

    def __get_count(self):
        """
        :return: Возвращает текущее количество элементов в очереди
        """
        return self.__count

    def __is_empty(self):
        """
        Вы полняет проверку очереди на пустоту
        :return: bool
        """
        return True if self.__count == 0 else False

    head = property(__peek)
    tail = property(__get_tail)
    count = property(__get_count)
    empty = property(__is_empty)



