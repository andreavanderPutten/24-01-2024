import flet as ft
from database.DAO  import DAO

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
    def fillDD(self):
        metodi = DAO.getAllMetodi()
        anni = DAO.getAllAnni()







    def handle_graph(self, e):
        a = self._view.dd_anno.value
        m = self._view.dd_ordinazione.value
        self._model.buildGraph(a,m)

        self._view.txtOut.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodes()} Numero di archi: {self._model.getNumEdges()}"))

        self._view.update_page()
    def handle_volume(self, e):
        pass

    def handle_path(self, e):
        pass
