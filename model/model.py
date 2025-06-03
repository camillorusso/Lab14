import networkx as nx
from database.DAO import DAO
class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self._grafo = nx.DiGraph()
        self._idMap = {}
        self.idMapID = {}
        self.stores = []

    def buildGraph(self, store_name, giorni):
        self._grafo.clear()
        self._nodes = DAO.getAllNodes(self._idMap[store_name])
        for element in self._nodes:
            self.idMapID[element.order_id] = element
        self._grafo.add_nodes_from(self._nodes)
        self._edges = DAO.getAllEdges(self._idMap[store_name], giorni)
        for element in self._edges:
            self._grafo.add_edge(self.idMapID[element.order_id1], self.idMapID[element.order_id2], weight=element.peso)

    def getAllStores(self):
        self.stores = DAO.getAllStores()
        for element in self.stores:
            self._idMap[element.store_name] = element.store_id
        return self.stores

    def getAllOrders(self):
        return self._nodes

    def getPercorsoLungo(self, n):
        tree = nx.dfs_tree(self._grafo, self.idMapID[n])
        a = list(tree.nodes)
        return a

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)