class Node:
    def __init__(self, data):
        """
        Формирует фобьект node
        """
        self.data = data
        self.prev = None


class Stack:
    def __init__(self):
        """
        Формирует объект Stack
        """
        self.__count = 0
        self.__top = None

    def push(self, item: Node) -> None:
        """
        Добавляет объект node в стэк
        :param item: Пренимает node
        :return: None
        """
        node = Node(item)
        node.prev = self.__top
        self.__top = node
        self.__count += 1

    def pop(self):
        """
        Удаляет объект node из стек путем переноса указателя __top на предыдущую ноду, то есть ссылка на текущую ноду теряется и указатель __top теперь ссылается на предыдущую
        А так как объект живет пока на него есть хоть одна ссылка, а ссылки на верхний элемент теперь нет, поэтому он удаляется из стэка
        :return: None
        """
        self.__top = self.__top.prev
        self.__count -= 1

    def peeck(self):
        """
        :return: Возвращает ноду, на которую указывает указатель __top
        """
        return self.__top

    def is_empty(self) -> bool:
        """
        :return: Возвращает True если в стеке есть хоть 1 элемент, иначе False
        """
        return True if self.__count == 0 else False

    def __get_count(self):
        """
        :return: Возвращает количество элементов в стеке
        """
        return self.__count

    count = property(__get_count)





