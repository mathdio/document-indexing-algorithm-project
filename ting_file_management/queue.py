from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        removed_value = self.data[0]
        del self.data[0]
        return removed_value

    def search(self, index):
        if not 0 <= index < len(self.data):
            raise IndexError("Índice Inválido ou Inexistente")
        else:
            return self.data[index]

    def __str__(self):
        return f"{self.data}"
