import pytest
from hw_data_structures.src.TaskStack import TaskStack
from hw_data_structures.src.PrintQueue import PrintQueue

data_test_positive = [('manegment', 17, True),
                      ('buhgalteria', 17, True),
                      ('otdel kadrov', 17, True),
                      ('secretar', 1, True)]

@pytest.mark.task_push
@pytest.mark.parametrize('val1, val2, result', data_test_positive)
def test_task_push(val1, val2, result):
    task_stack = TaskStack()
    assert task_stack.push(val1, val2) == result


data_test_positive = [('manegment', 17, True),
                      ('buhgalteria', 17, True),
                      ('otdel kadrov', 17, True),
                      ('secretar', 1, True)]

@pytest.mark.queue_enqueue
@pytest.mark.parametrize('val1, val2, result', data_test_positive)
def test_queue_enqueue(val1, val2, result):
    queue = PrintQueue()
    assert queue.enqueue(val1, val2) == result