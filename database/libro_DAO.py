from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_all_generi(self):

        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result

        query = " SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL "
        cursor = cnx.cursor(dictionary=True)

        try:
            cursor.execute(query)


            for row in cursor:
                if row["genere"]:
                    result.append(row["genere"])
        except Exception as e:
            print(f" Errore durante il recupero dei generi {e}")

        finally:
            cursor.close()
            cnx.close()
        return result



