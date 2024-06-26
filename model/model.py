import networkx as nx

from database.DAO import DAO
from database.DB_connect import DBConnect


class Model:
    def __init__(self):
        self.grafo = nx.DiGraph()


    def creaGrafo(self, anno, metodo, soglia):
        self.grafo.clear()
        self.grafo.add_nodes_from(DAO.getNodi(anno, metodo))
        for u in self.grafo.nodes:
            for v in self.grafo.nodes:
                if u == v:
                    continue
                else:
                    if v[1] >= float(u[1])*(1+soglia):
                        print(f"primo nodo: {u[1]} < soglia: {float(u[1])*(1+soglia)} < secondo nodo: {v[1]}")
                        self.grafo.add_edge(u, v)

    def grafoDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)

    def top5Nodi(self):
        lista = []
        for nodo in self.grafo.nodes:
            if self.grafo.out_degree(nodo) == 0:
                lista.append((self.grafo.in_degree(nodo), nodo))
        lista.sort(reverse=True)
        return lista
