from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.__data = list()

    def __len__(self):
        return len(self.__data)

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        removed_value = self.__data[0]
        del self.__data[0]
        return removed_value

    def search(self, index):
        if not 0 <= index < len(self.__data):
            raise IndexError("Índice Inválido ou Inexistente")
        else:
            return self.__data[index]

    def __str__(self):
        return f"{self.__data}"
