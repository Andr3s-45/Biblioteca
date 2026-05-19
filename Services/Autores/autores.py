"""""
Se tendra el modelo para la gestion de usuarios, 
es decir todo aquello que tenga que ver con la persistenncia (SQL).
"""""

from conexion import *

class Autores:
    def listar(self):
        sql = "SELECT * FROM autores"
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        return resultado
    
    
    def consultar(self, idAutor):
        sql = f"SELECT * FROM autores WHERE idAutor ='{idAutor}'"
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        return resultado
    
    def agregar(self,idAutor,nombre,email,idPais):
        sql = f"INSERT INTO autores (idAutor,nombre,email,idPais) VALUES ('{idAutor}','{nombre}','{email}', '{idPais}')"
        mi_cursor.execute(sql)
        mi_db.commit()


    def modificar(self,idAutor,nombre,email,idPais):
        sql = f"UPDATE autores SET nombre='{nombre}',email= '{email}', idPais= '{idPais}'WHERE idAutor='{idAutor}'"
        mi_cursor.execute(sql)
        mi_db.commit()
        return self.consultar(idAutor)

    def eliminar(self, idAutor):
        sql = f"DELETE FROM autores WHERE idAutor='{idAutor}'"
        mi_cursor.execute(sql)
        mi_db.commit()


mis_autores = Autores()