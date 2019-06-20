"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""
class Graph:
    def __init__(self, E):
        self.E = E
        self.start = 0
        self.index = len(E.keys())
        self.key = list(E.keys())

    def __next__(self):
        if self.start >= self.index:
            raise StopIteration()
        x = self.start
        self.start += 1
        return self.key[x]


    def __iter__(self):
        return self


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertice in graph:
    print(vertice)
