"""
Написать тесты(pytest) к предыдущим 3 заданиям, запустив которые, я бы смог бы проверить их корректность
"""
import pytest
import os
import task1
import task2
import task3

# TASK1
@pytest.fixture
def data_task1():
    current_path = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.join(current_path, '../../06-advanced-python')
    contents_generator = os.walk(project_path)
    contents = []
    next(iter(contents_generator))
    for root, dirs, files in contents_generator:
        contents.append((root, dirs, files))

    return project_path, contents


def test_task1(data_task1):
    files1 = '|   |   |   |   |   |   |   |   |-> task1.py'
    files2 = '|   |   |   |   |   |   |   |   |-> task2.py'
    files3 = '|   |   |   |   |   |   |   |   |-> task3.py'
    files4 = '|   |   |   |   |   |   |   |   |-> task4.py'

    project_path, contents = data_task1
    folder1 = task1.PrintableFolder(project_path, contents)
    file = task1.PrintableFile('task4.py')
    tree_list = folder1.full_tree_list

    assert file in folder1
    assert files1 in tree_list
    assert files2 in tree_list
    assert files3 in tree_list
    assert files4 in tree_list


# TASK2
graph1 = task2.Graph({'A': ['C', 'D'], 'B': [], 'C': ['B'], 'D': ['B']})
graph2 = task2.Graph({'A': ['B', 'D'], 'C': [''], 'D': ['B'], 'B': ['A']})
graph3 = task2.Graph({'A': [], 'B': [], 'C': [], 'D': []})

@pytest.mark.parametrize('graph, result', [
    (graph1, 'ABCD'),
    (graph2, 'ACDB'),
    (graph3, 'ABCD')])
def test_task2_graph_itterations(graph, result):
    assert list(graph) == list(result)

# TASK3
ceasar = task3.CeasarSipher()

@pytest.mark.parametrize('msg1, msg2, out1, out2', [
    ('boss', 'putin', 'fsww', 'wbapu')])
def test_task3_ceasar_sipher(msg1, msg2, out1, out2):
    """should be ok"""
    ceasar.message = msg1
    ceasar.another_message = msg2
    assert ceasar.message == out1
    assert ceasar.another_message == out2
