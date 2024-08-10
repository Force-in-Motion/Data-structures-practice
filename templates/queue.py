class Node:
    def __init__(self, data):
        self.data = data  # Данные ноды
        self.prev = None  # Ссылка на предыдущий элемент


class Queue:
    def __init__(self):
        self.__head = None  # Указатель головы очереди
        self.__tail = None  # Указатель хвоста очереди
        self.__count = 0  # Количество нод в очереди на текущий момент

    def enqueue(self, item) -> bool:
        """
        Добавляет элемент в очередь c хвоста
        :return: bool
        """
        node = Node(item) # Создаем ноду

        self.__count += 1  # Увеличиваем количество нод на 1

        if self.__count == 1:  # Если количество нод в очереди 0, то заходим в блок кода
            self.__head = node  # Присваиваем голове и хвосту одновременно ссылку на ноду, так как она первая и единственная в очереди согласно условию
            self.__tail = node
            return True

        self.__tail.prev = node  # Если добавляется не первая нода, то ссылке текущего хвоста (то есть ноде на которую ссылается хвост в данный момент) мы присваиваем новую ноду, чтобы была связь между ними
        self.__tail = node  # А затем хвосту присваиваем новую ноду, таким образом указатель хвоста смещается влево, на новую ноду, а старый хвост уходит в сторону середины очереди

        return True
    def dequeue(self) -> Node or Exception:
        """
        Удаляет элемент из головы очереди и возвращает его
        """
        assert self.__count != 0, ValueError('Очередь пуста, удалять нечего, для начала добавьте ноды')

        one_node = self.__head  # Поскольку нам нужно вернуть удаляемую ноду, то нам нужно сохранить ее в переменную перед удалением ибо после удаления ссылки на нее уже не будет

        self.__head = self.__head.prev  # После этого мы голове по ссылке присваиваем предыдущую ноду, на первую ноду теперь никто не ссылается поэтому она удаляется

        self.__count -= 1  # Уменьшаем количество нод на 1

        return one_node

    def __peek(self) -> Node:
        """
        :return: Возвращает первый элемент с головы в очереди
        """
        return self.__head

    def __get_tail(self) -> Node:
        """
        :return: Возвращает ноду, на которую ссылается self.__tail в данный момент
        """
        return self.__tail

    def __get_count(self) -> int:
        """
        :return: Возвращает текущее количество элементов в очереди
        """
        return self.__count

    def __is_empty(self) -> bool:
        """
        Вы полняет проверку очереди на пустоту
        :return: bool
        """
        return True if self.__count == 0 else False

    head = property(__peek)
    tail = property(__get_tail)
    count = property(__get_count)
    empty = property(__is_empty)


