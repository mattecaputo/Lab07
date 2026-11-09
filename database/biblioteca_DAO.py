from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_all_biblioteche(self):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result

        query = " SELECT * FROM biblioteca "
        cursor = cnx.cursor(dictionary=True)



        try:
            cursor.execute(query)
            for row in cursor:
                result.append(Biblioteca(**row))
        except Exception as e:
            print(f"Errore: {e}")
        finally:
            cursor.close()
            cnx.close()
        return result


