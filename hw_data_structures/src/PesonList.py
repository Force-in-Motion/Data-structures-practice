from __future__ import annotations

class PersonCard:
    def __init__(self, name, age, occupation, next: PersonCard = None):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.next = next


class PersonList:
    def __init__(self):
        self.__count = 0
        self.__head = None

    def add_person(self, name, age, occupation) -> bool or Exception:
        """
        Добавляет новую карточку персоны в начало списка
        :return: bool or Exeption
        """
        node = PersonCard(name, age, occupation)

        self.__count += 1

        if self.__count == 1:
            self.__head = node
            return True

        node.next = self.__head
        self.__head = node
        return True

    def append_person(self, name, age, occupation) -> bool or Exception:
        """
        Добавляет новую карточку персоны в конец списка
        :return: bool or Exeption
        """

        if self.__count == 0:
            self.add_person(name, age, occupation)
            return True

        self.__count += 1

        node = PersonCard(name, age, occupation)

        iterator = self.__head

        while not (iterator.next is None):
            iterator = iterator.next

        iterator.next = node
        return True

    def insert_person_position(self, position, name, age, occupation) -> bool:
        """
        Добавляет новую карточку персоны на указанную позицию
        :return: bool or Exeption
        """

        if self.__count == 0 or position == 1:
            self.add_person(name, age, occupation)
            return True

        self.__count += 1

        node = PersonCard(name, age, occupation)

        count_position = 1

        iterator = self.__head
        iterator_prev = None

        while count_position != position and not iterator.next is None:
            iterator_prev = iterator
            iterator = iterator.next
            count_position += 1

            if count_position == position:
                node.next = iterator
                iterator_prev.next = node

                return True
        return False

    def remove_first_person(self) -> PersonCard or Exception:
        """
        Удаляет первую карточку в списке
        :return: Возвращает первую карточку списка или Exception
        """
        first_person = self.__head

        self.__head = self.__head.next

        self.__count -= 1

        return first_person

    def remove_last_person(self)-> PersonCard or Exception:
        """
        Удаляет последнюю карточку в списке
        :return: Возвращает последнюю карточку списка или Exception
        """
        iterator = self.__head

        while not (iterator.next is None):
            iterator = iterator.next

        if iterator.next == None:
            result_node = iterator
            self.__count -= 1

            return result_node

    def remove_person_for_data(self, name) -> PersonCard or Exception:
        """
        Удаляет карточку персоны, соответствующую переданной person
        :param data:
        :return:
        """
        assert self.__count != 0, ValueError('В списке отсутствуют элементы, удалять нечего')

        if self.__head.name == name:
            self.remove_first_person()

        iterator = self.__head
        iterator_prev = None

        while iterator.name != name and not (iterator.next is None):
            iterator_prev = iterator
            iterator = iterator.next

            if iterator.name == name:
                required_node = iterator
                iterator_prev.next = iterator.next

                return required_node

    def __peek(self):
        """
        :return: Возвращает ноду, на которую указывает голова списка
        """
        return self.__head

    def __clear_all(self) -> None:
        """
        Очищает список, удаляя все карточки
        :return: None
        """
        self.__head = None

    def __total_people(self) -> int:
        """
        :return: Возвращает количество карточек в списке.
        """
        return self.__count

    def __is_empty(self):
        """
        :return:  Возвращает true, если список пуст, иначе false
        """
        return True if self.__count == 0 else False

    peek = property(__peek)
    clear = property(__clear_all)
    count = property(__total_people)
    empty = property(__is_empty)
