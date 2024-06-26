import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        metodi = DAO.getMetodi()
        anni = DAO.getAnni()

        self._view._ddmethod.options = list(map(lambda x: ft.dropdown.Option(key=x[0], text=x[1]), metodi))
        self._view._ddyear.options = list(map(lambda x: ft.dropdown.Option(x), anni))

    def handle_graph(self, e):
        anno = int(self._view._ddyear.value)
        metodo = int(self._view._ddmethod.value)
        if float(self._view._txtSoglia.value) < 0:
            self._view.create_alert("vaffanculo")
            return
        else:
            soglia = float(self._view._txtSoglia.value)

        self._model.creaGrafo(anno, metodo, soglia)

        self._view.txtOut.controls.append(ft.Text(f"nodi: {self._model.grafoDetails()[0]}, archi {self._model.grafoDetails()[1]}"))
        self._view.update_page()

    def handle_search(self, e):
        pass