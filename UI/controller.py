import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        self._view.dd_biblioteca.options.clear()
        self._view.dd_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))
        for biblioteca in self._model.get_biblioteche():
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(biblioteca.nome))

        self._view.dd_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        for genere in self._model.get_generi():
            if genere:
                self._view.dd_genere.options.append(ft.dropdown.Option(genere))

        self._view.dd_biblioteca.value = " Nessun filtro"
        self._view.dd_genere.value = " Nessun filtro"

        self._view.page.update()

    # CALLBACKS DROPDOWN
    def update_biblioteca(self,e):
        self.biblioteca_selezionata = e.control.value

    def update_genere(self,e):
        self.genere_selezionato = e.control.value

