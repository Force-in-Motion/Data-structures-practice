
class ProjectTask:
    def __init__(self, description: str, due_date: str):
        """
        Формирует шаблон задачи
        :param description: Пренимает описание
        :param due_date: Пренимает дату исполнения
        """
        self.description = description
        self.due_date = due_date
        self.prev = None


class TaskStack:
    def __init__(self):
        """
        Формирует шаблон стэка задач
        """
        self.__count = 0
        self.__top = None

    def push(self, description: str, due_date: str) -> None:
        """
        Добавляет новую задачу в стэк
        :param description: Пренимает описание задачи
        :param due_date: Пренимает дату исполнения
        :return: None
        """
        task = ProjectTask(description, due_date)
        task.prev = self.__top
        self.__top = task
        self.__count += 1

    def pop(self):
        """
        Удаляет задачу из стека, путем переноса указателя (ссылки топа) с текущей, которую требуется удалить, на предыдущую
        :return: Возвращает Удаленную задачу если стек не пустой или то чему равен топ по умолчанию если задач нет, то есть None
        """
        current_top = self.__top

        if self.__count != 0:
            self.__top = self.__top.prev
            self.__count -= 1
            return current_top

        return self.top

    def peek(self):
        """
        :return: Возвращает текущее значение указателя
        ( если в стеке есть ноды то указывает на верхнюю, если стек пусто, то вернет значение по умолчанию, то есть None)
        """
        return self.__top

    def is_empty(self):
        """
        :return: Выполняет проверку стэка на пустоту, если стэк пуст то вернет True иначе False
        """
        return True if self.__count == 0 else False

    def __get_count(self):
        """
        :return: Возвращает текущее количество нод в стеке
        """
        return self.__count

    top = property(peek)
    count = property(__get_count)

