from Services.Editoriales.conexion import *
import pytest
import requests

class Test_editoriales: #Preparacion de la prueba
    def setup_class(self):
        self.url = "http://localhost:5083/editoriales"
        
        sql = "INSERT IGNORE INTO paises (idPais,nombre) VALUES ('MX', 'MEXICO')"
        mi_cursor.execute(sql)
        sql = "INSERT IGNORE INTO paises (idPais,nombre) VALUES ('ARG', 'ARGENTINA')"
        mi_cursor.execute(sql)
        
        idEditorial = "Arg2"
        nombre = "test"
        idPais = "MX"
        sql = f"INSERT INTO editoriales (idEditorial,nombre,idPais) VALUES ('{idEditorial}', '{nombre}', '{idPais}')"
        mi_cursor.execute(sql)
        mi_db.commit()


    def teardown_class(self): #Limpiar la base de datos
        sql = f"DELETE FROM editoriales WHERE idEditorial IN ('Arg2', 'Arg3')"
        mi_cursor.execute(sql)
        mi_db.commit()

    def test_lista_editoriales(self):
        esperado = "editoriales"
        # Ejecutar la prueba
        calculado = requests.get(self.url)
        # Verificación
        assert calculado.status_code == 200
        assert calculado.json()["mensaje"]==esperado



    @pytest.mark.parametrize(
        ["nuevo_entrada", "esperado_entrada"],
        [({"idEditorial":"Arg3", "nombre":"Editoriales Pruebas", "idPais":"MX"}, "Editorial agregado con éxito"), 
        ({"idEditorial":"Arg2", "nombre":"test","idPais":"ARG"},"Id de editorial ya existe")]
    )

    def test_agregar(self, nuevo_entrada,esperado_entrada):

        calculado = requests.post(self.url,json=nuevo_entrada)
        assert calculado.status_code ==200
        assert esperado_entrada == calculado.json()["mensaje"]




    @pytest.mark.parametrize(
        ["id_entrada","esperado_entrada"],
        [("Arg2", "Editorial encontrado"),
        ("Arg4", "Editorial no encontrado!!!")]
    )

    def test_busqueda(self, id_entrada, esperado_entrada): 
        #La ejecucion de caso de prueba 2
        idEditorial = id_entrada
        esperado = esperado_entrada
        calculado = requests.get(f"{self.url}/{idEditorial}")
        #Verificacion del caso de prueba
        assert calculado.status_code==200
        assert esperado in calculado.json()["mensaje"]


    def test_modifica1(self):
        idEditorial = "Arg2"
        nombre = "Frank"
        idPais = "MX"
        nuevo = {"nombre":nombre, "idPais":idPais}
        esperado = "Editorial modificado con éxito"
        # Ejecutar la prueba
        calculado = requests.put(f"{self.url}/{idEditorial}",json=nuevo)
        # Verificar la prueba
        assert calculado.status_code == 200
        assert esperado in calculado.json()["mensaje"]
        sql =f"SELECT * FROM editoriales WHERE idEditorial='{idEditorial}'"
        mi_cursor.execute(sql)
        datos = mi_cursor.fetchall()[0]
        assert nombre==datos[1] and idPais==datos[2]


    # Para cuando el usuario no existe
    def test_modifica2(self):
        idEditorial = "Col2"
        nombre = "test2"
        idPais = "MX"
        nuevo = {"nombre":nombre, "idPais":idPais}
        esperado = "Editorial no existe"
        # Ejecutar la prueba
        calculado = requests.put(f"{self.url}/{idEditorial}",json=nuevo)
        # Verificar la prueba
        assert calculado.status_code == 200
        assert esperado in calculado.json()["mensaje"]


    @pytest.mark.parametrize(
        ["id_entrada","esperado_entrada"],
        [("Arg2","Editorial eliminado con éxito"),
        ("Arg4","Editorial no existe")]
    )


    def test_elimina(self,id_entrada, esperado_entrada):
        idEditorial = id_entrada
        esperado = esperado_entrada
        # Ejecutar la prueba
        calculado = requests.delete(f"{self.url}/{idEditorial}")
        # Verificar la prueba
        assert calculado.status_code == 200
        assert esperado in calculado.json()["mensaje"]
        mi_db.commit()
        sql =f"SELECT * FROM editoriales WHERE idEditorial='{idEditorial}'"
        mi_cursor.execute(sql)
        datos = mi_cursor.fetchall()
        assert len(datos)==0

    