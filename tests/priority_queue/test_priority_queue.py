import pytest
from ting_file_management.priority_queue import PriorityQueue

data = [
    {
        "nome_do_arquivo": "arquivo1",
        "qtd_linhas": 2,
        "linhas_do_arquivo": []
    },
    {
        "nome_do_arquivo": "arquivo2",
        "qtd_linhas": 10,
        "linhas_do_arquivo": []
    },
    {
        "nome_do_arquivo": "arquivo3",
        "qtd_linhas": 4,
        "linhas_do_arquivo": []
    },
    {
        "nome_do_arquivo": "arquivo4",
        "qtd_linhas": 6,
        "linhas_do_arquivo": []
    },
]


def test_basic_priority_queueing():
    priority = PriorityQueue()

    """Teste da função enqueue"""
    priority.enqueue(data[0])
    priority.enqueue(data[1])
    priority.enqueue(data[2])
    priority.enqueue(data[3])

    """Teste do tamanho da lista"""
    assert len(priority.regular_priority) == 2
    assert len(priority.high_priority) == 2
    assert len(priority) == 4

    """Teste da função search"""
    search = priority.search(0)
    assert search == data[0]

    assert priority.is_priority(data[0]) is True
    assert priority.is_priority(data[1]) is False

    """Teste em caso de erro na função search"""
    with pytest.raises(IndexError):
        priority.search(100)

    """Teste da função dequeue"""
    dequeue = priority.dequeue()
    assert dequeue == data[0]
