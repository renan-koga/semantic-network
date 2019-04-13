import sys
from Graph import Graph

TESTE_FILE = ""
NETWORK = sys.argv[1]
GRAPH = Graph()

def createGraph():
	arq = open(NETWORK)

	for line in arq:
		teste = line.split("\n")
		words = teste[0].split(" ")
		GRAPH.addNode(words[0])
		GRAPH.addNode(words[2])
		GRAPH.addEdge(words[0], words[2], words[1])

if __name__ == "__main__":
	createGraph()

	while (True):
		print("\nDigite uma sentença")
		sentence = input("> ")

		if sentence == "quit":
			break

		splitted = sentence.split(" ")
		node1 = splitted[0]
		link = splitted[1]
		node2 = splitted[2]

		paths = GRAPH.getPath(node1, node2)

		logic = True
		if paths is not None:
			if len(paths) > 0:
				for path in paths:
					once = False
					for i in range(len(path) - 1):
						node1 = path[i]
						node2 = path[i+1]
						aux_link = GRAPH.getEdge(node1, node2)

						if link == "e_um":
							if aux_link != "e_um":
								logic = False
						elif link == "tem":
							if aux_link != "e_um" and aux_link != "tem":
								logic = False
						else:
							if aux_link != "e_um":
								if aux_link == link:
									if once:
										logic = False
									else:
										once = True
								else:
									logic = False

					if logic:
						print("Verdadeiro")
						break

				if not logic:
					print("Falso")
			else: print("Falso")