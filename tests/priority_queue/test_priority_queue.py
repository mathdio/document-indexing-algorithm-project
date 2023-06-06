from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()
    assert len(queue) == 0
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(5)

    queue.enqueue({"qtd_linhas": 5})
    queue.enqueue({"qtd_linhas": 4})
    assert len(queue) == 2

    assert queue.regular_priority.data == [{"qtd_linhas": 5}]
    assert queue.high_priority.data == [{"qtd_linhas": 4}]

    assert queue.search(0) == {"qtd_linhas": 4}
    assert queue.search(1) == {"qtd_linhas": 5}

    queue.dequeue()
    assert len(queue) == 1
    queue.dequeue()
    assert len(queue) == 0
