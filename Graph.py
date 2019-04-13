import sys

class Graph():
    def __init__(self):
        self.vertexes = dict()
        self.edges = dict()
        self.size = 0

    def addNode(self, vertex):
        if not vertex in self.vertexes:
            self.vertexes[vertex] = []
            self.size += 1

    def addEdge(self, vertex1, vertex2, edge):
        if not vertex1 in self.vertexes:
            self.vertexes[vertex1] = []
            self.size += 1
        if not vertex2 in self.vertexes:
            self.vertexes[vertex2] = []
            self.size += 1

        self.vertexes[vertex1].append(vertex2)
        self.edges[vertex1, vertex2] = edge

    def getEdge(self, vertex1, vertex2):
        if not vertex1 in self.vertexes or not vertex2 in self.vertexes:
            print("Nó não encontrado!")
            return None
        else:
            if (vertex1, vertex2) in self.edges:
                # print(self.edges[vertex1, vertex2])
                return self.edges[vertex1, vertex2]
            else:
                print("Não há conexão entre os nós")
                return None

    def printGraph(self):
        # print(self.vertexes)
        for vertex in self.vertexes:
            print(vertex + " => ", end = "")
            for neighbor in self.vertexes[vertex]:
                print(neighbor + " ", end = "")

            print()

    def getPath(self, source, dest):
        if not source in self.vertexes or not dest in self.vertexes:
            print("Não há um ou ambos os nós")
            return None

        stack = []
        stack.append(source)
        path = []
        self.depthFirst(source, dest, stack, path)
        return path

    def depthFirst(self, source, dest, stack, path):
        if source == dest:
            path.append(stack[:])
            return

        for node in self.vertexes[source]:
            stack.append(node)
            # print("STACK: " + str(stack))
            self.depthFirst(node, dest, stack, path)
            # print("PATH: " + str(path))
            stack.pop()