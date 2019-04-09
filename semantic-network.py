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
    # print(GRAPH.edges())
    # print(GRAPH["neymar"]["atacante"]["relacao"])
    # print(list(GRAPH.successors("atacante")))

    # exit(1)

# neymar tem sola???
# V ou F???

# neymar tem chuteira
# chuteira e_um tenis

def checkSentence(node1, link, node2):
	logic = False	
	if GRAPH.has_edge(node1, node2):
		if GRAPH[node1][node2]["relacao"] == link or GRAPH[node1][node2]["relacao"] == "e_um":
			return True

	for node in GRAPH.successors(node1):
		logic = checkSentence(node, link, node2)

		if logic:
			return logic

	return False
    # else:
    #     for node in GRAPH.successors(node1):
    #         logic = checkSentence(node, "e_um", node2)
    #         if logic:
    #             return logic



    # for node in node1:
    #     if GRAPH.has_edge(node, node2):
    #         if GRAPH[node][node2] == link:
    #             return True

# if len(sys.argv) > 2:
#     TESTE_FILE = sys.argv[2]

if __name__ == "__main__":
    createGraph()
    
    while (True):
        print("\nDigite uma setença")
        sentence = input("> ")

        splitted = sentence.split(" ")
        node1 = splitted[0]
        link = splitted[1]
        node2 = splitted[2]

        logic = checkSentence(node1, link, node2)
        if logic:
            print("OK!")
        else:
            print("Deu Ruim!")
        
        # exit(1)
