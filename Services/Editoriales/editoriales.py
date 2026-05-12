"""""
es decir todo aquello que tenga que ver con la persistenncia (SQL).
"""""

from conexion import *

class Editorial:
    def listar(self):
        sql = "SELECT * FROM editoriales"
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        return resultado
    
    
    def consultar(self, idEditorial):
        sql = f"SELECT * FROM editoriales WHERE idEditorial ='{idEditorial}'"
        mi_cursor.execute(sql)
        resultado = mi_cursor.fetchall()
        return resultado
    
    def agregar(self,idEditorial,nombre,idPais):
        sql = f"INSERT INTO editoriales (idEditorial,nombre,idPais) VALUES ('{idEditorial}','{nombre}','{idPais}')"
        mi_cursor.execute(sql)
        mi_db.commit()


    def modificar(self,idEditorial,nombre,idPais):
        sql = f"UPDATE editoriales SET nombre='{nombre}',idPais= '{idPais}'WHERE idEditorial='{idEditorial}'"
        mi_cursor.execute(sql)
        mi_db.commit()
        return self.consultar(idEditorial)

    def eliminar(self, idEditorial):
        sql = f"DELETE FROM editoriales WHERE idEditorial='{idEditorial}'"
        mi_cursor.execute(sql)
        mi_db.commit()


mis_editoriales = Editorial()