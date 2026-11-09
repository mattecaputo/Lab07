from database import biblioteca_DAO, libro_DAO
from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca_nome, genere):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        bib_id = None
        if biblioteca_nome and biblioteca_nome != "Nessun Filtro":
            for b in self._biblioteca_dao.get_all_biblioteche():
                if b.nome == biblioteca_nome:
                    bib_id = b.id
                    break
        gen = None if not genere or genere == "Nessun filtro" else genere

        return self._libro_dao.get_libri_filtrati(bib_id, gen)

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        return self._libro_dao.get_all_generi()

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        return self._biblioteca_dao.get_all_biblioteche()
