import sys
import networkx

#Gera a rede semântica a partir do arquivo de entrada
def createGraph():
	arq = open(NETWORK)
	for line in arq:
		teste = line.split("\n")
		words = teste[0].split(" ")
		GRAPH.add_node(words[0])
		GRAPH.add_node(words[2])
		GRAPH.add_edge(words[0], words[2], relacao = words[1])

NETWORK = sys.argv[1]
GRAPH = networkx.DiGraph()
if __name__ == "__main__":
	#GRAPH: DiGrafo -- Gerando o grafo a partir do arquivo de entrada
	createGraph()	
	while (True):
		print("\nDigite uma sentença")
		sentence = input("> ")
		#Obtendo a sentença a ser analisada
		splitted = sentence.split(" ")
		node1 = splitted[0]
		link = splitted[1]
		node2 = splitted[2]
		#Paths: Generator -- Obtendo os caminhos possíveis de origem -> destino (tipo: Generator)
		try:
			paths = networkx.all_simple_paths(GRAPH, source=node1, target=node2)
			if not paths:
				print("Falso")
			else:
				logic = True
				e_um = False
				tem = False
				others = False
				#Iterando por entre os caminhos existentes de origem -> destino
				for path in paths:
					once = False
					#Comparando os nós de cada caminho de par em par de origem -> destino
					for i in range(len(path) - 1):
						node1 = path[i]
						node2 = path[i+1]
						aux_link = GRAPH[node1][node2]["relacao"]
						#Analisando o tipo de relação de cada par de nós
						#Permutando valores booleanos dependendo da série de relações origem -> destino
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
		except:
			print('Rede Semântica: Erro na busca')