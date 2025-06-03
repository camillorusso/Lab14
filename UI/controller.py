import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self.lista_stores = []
        self._currentStore = None
        self.lista_nodes = []
        self._currentNode = None

    def fillDD_store(self):
        self.lista_stores = self._model.getAllStores()
        for element in self.lista_stores:
            self._view._ddStore.options.append(ft.dropdown.Option(text=element.store_name,
                                                                 data=element.store_name,
                                                                 on_click=self.read_DD_store))

    def read_DD_store(self, e):
        print("read_DD_store called ")
        if e.control.data is None:
            self._currentStore = None
        else:
            self._currentStore = e.control.data
        print(self._currentStore)

    def fillDD_node(self):
        self.lista_nodes = self._model.getAllOrders()
        for element in self.lista_nodes:
            self._view._ddNode.options.append(ft.dropdown.Option(text=element.order_id,
                                                                 data=element.order_id,
                                                                 on_click=self.read_DD_node))

    def read_DD_node(self, e):
        print("read_DD_node called ")
        if e.control.data is None:
            self._currentNode = None
        else:
            self._currentNode = e.control.data
        print(self._currentNode)

    def handleCreaGrafo(self, e):
        g = self._view._txtIntK.value
        try:
            giorni = int(g)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserisci un numero intero valido!"))
            self._view.update_page()
            return
        if self._currentStore is None or self._currentStore == "":
            self._view.create_alert("Selezionare uno store!")
            return
        self._model.buildGraph(self._currentStore, giorni)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo creato correttamente."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getNumEdges()} archi."))
        self.fillDD_node()
        self._view.update_page()

    def handleCerca(self, e):
        if self._currentNode is None or self._currentNode == "":
            self._view.create_alert("Selezionare un nodo!")
            return
        lista1 = self._model.getPercorsoLungo(self._currentNode)
        self._view.txt_result.controls.append(ft.Text(f"Il percorso ha come tappe:"))
        for element in lista1:
            self._view.txt_result.controls.append(ft.Text(f"{element.order_id}"))
        self._view.update_page()
    def handleRicorsione(self, e):
        pass
