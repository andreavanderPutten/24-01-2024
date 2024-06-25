import flet as ft
from database.DAO import DAO

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        self.dd_ordinazione = None
        self.dd_anno = None
        self.txt_valore = None
        self.btn_crea_grafo = None
        self.btn_percorso = None
        self.txt_soglia = None
        self.listMetodi = DAO.getAllMetodi()
        self.listaAnni = DAO.getAllAnni()



    def load_interface(self):
        # title
        self._title = ft.Text("TdP 2024 - 24-01-24: Prova tema d'esame", color="blue", size=24)
        self._page.controls.append(self._title)

        self.dd_ordinazione = ft.Dropdown(label="Ordine")
        self.dd_anno  = ft.Dropdown(label="Anno")
        self.btn_percorso = ft.ElevatedButton(text="Calcola percorso", on_click=self._controller.handle_path)
        self.btn_crea_grafo = ft.ElevatedButton(text="crea grafo",on_click=self._controller.handle_graph)
        self.txt_soglia = ft.TextField(label="soglia")
        row1 = ft.Row([self.dd_ordinazione, self.dd_anno, self.btn_crea_grafo,self.btn_percorso,self.txt_soglia],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self._page.update()

        self.txtOut = ft.ListView(expand=1, spacing=10, padding=10, auto_scroll=True)
        self._page.controls.append(self.txtOut)

        for t in self.listMetodi :
            self.dd_ordinazione.options.append(ft.dropdown.Option(t))

        for anno in self.listaAnni :
            self.dd_anno.options.append(ft.dropdown.Option(anno))
        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()



