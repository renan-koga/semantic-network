import sys
import networkx

TESTE_FILE = ""
NETWORK = sys.argv[1]
GRAPH = networkx.DiGraph()

def createGraph():
	arq = open(NETWORK)

	for line in arq:
		teste = line.split("\n")
		words = teste[0].split(" ")
		GRAPH.add_node(words[0])
		GRAPH.add_node(words[2])
		GRAPH.add_edge(words[0], words[2], relacao = words[1])
	# print(GRAPH[words[0]][words[2]]['relacao'])
	# print(words)

	# print(GRAPH.nodes())
	# print(GRAPH.edges("neymar"))
	# print(GRAPH["neymar"]["atacante"]["relacao"])
	# print(list(GRAPH.successors("atacante")))

	# exit(1)

def checkSentence(node1, link, node2, aux_link, cont):
	logic = False	
	print(node1 + " :: " + node2)
	if node1 == node2:
		return True

	for aux_node in GRAPH.successors(node1):
		# for aux_node in GRAPH.successors(node):
		if GRAPH[node1][aux_node]["relacao"] != "e_um":
			if cont > 0:
				return False
			else:
				if GRAPH[node1][aux_node]["relacao"] != "tem":
					cont += 1
					aux_link = GRAPH[node1][aux_node]["relacao"]

		# print(node1 + " " + link + " " + node)
		logic = checkSentence(aux_node, link, node2, aux_link, cont)

		if logic:
			return logic
	return False

# if len(sys.argv) > 2:
#     TESTE_FILE = sys.argv[2]

if __name__ == "__main__":
	createGraph()
	
	while (True):
		print("\nDigite uma sentença")
		sentence = input("> ")

		splitted = sentence.split(" ")
		node1 = splitted[0]
		link = splitted[1]
		node2 = splitted[2]

		paths = networkx.all_simple_paths(GRAPH, source=node1, target=node2)
		# print(list(paths))
		# exit(1)

		logic = True
		e_um = False
		tem = False
		others = False
		for path in paths:
			once = False
			for i in range(len(path) - 1):
				node1 = path[i]
				node2 = path[i+1]
				aux_link = GRAPH[node1][node2]["relacao"]

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

				# if others:
				# 	if link != "e_um":
				# 		logic = False
				
				# else:
				# 	if link == "e_um":
				# 		e_um = True
				# 	elif link == "tem":
				# 		tem = True
				# 	else:
				# 		others = True

				# if GRAPH[node1][node2]["relacao"] == "e_um":
				# 	e_um = True
				# elif GRAPH[node1][node2]["relacao"] == "tem":
				# 	tem = True
				# else:
				# 	if not others:
				# 		others = True
				# 	else:
				# 		logic = False
				# 		break
			# print(path)

			if logic:
				print("Verdadeiro")
				break

		if not logic:
			print("Falso")

		# exit(1)

		# logic = checkSentence(node1, link, node2, "", 0)
		# if logic:
		# 	print("OK!")
		# else:
		# 	print("Deu Ruim!")
		
		# exit(1)
