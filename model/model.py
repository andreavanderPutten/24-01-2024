from database.DAO import DAO
import networkx as nx
class Model:
    def __init__(self):


        self.edges = None
        self.nodes = []
        self.grafo = nx.Graph()
        self.idMap = {}
        self.listaProdotti = None

    def loadProdotti(self,anno,metodo):
        self.listaProdotti = DAO.getAllProdotti(anno,metodo)

    def buildGraph(self,a,m):
        self.grafo.clear()
        self.loadProdotti(a,m)
        print(self.listaProdotti)

        for p in self.listaProdotti :
            self.nodes.append(p)
            print(p)

        self.grafo.add_nodes_from(self.nodes)

    def getNumEdges(self):
        return self.grafo.number_of_edges()

    def getNumNodes(self):
        return self.grafo.number_of_nodes()

    def getAllEdges(self):
        return self.grafo.edges