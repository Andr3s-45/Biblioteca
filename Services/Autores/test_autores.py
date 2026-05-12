from Services.Autores.conexion import *
import pytest
import requests

class Test_autores: #Preparacion de la prueba
    def setup_class(self):
        self.url = "http://localhost:5084/autores"
        sql = """INSERT INTO paises (idPais,nombre,continente) VALUES ('AR','Argentina','America'), ('MX', 'Mexico', 'America')"""
        mi_cursor.execute(sql)
        mi_db.commit()

        idAutor = "01"
        nombre = "Frank"
        email = "frank1996@gmail.com"
        idPais = "AR"
        sql = f"INSERT INTO autores (idAutor,nombre,email,idPais) VALUES ('{idAutor}', '{nombre}', '{email}', '{idPais}')"
        mi_cursor.execute(sql)
        mi_db.commit()


    def teardown_class(self): #Limpiar la base de datos

        sql = "DELETE FROM autores"
        mi_cursor.execute(sql)

        sql = f"DELETE FROM paises WHERE idPais IN ('AR', 'MX')"
        mi_cursor.execute(sql)
        mi_db.commit()


    def test_lista_autores(self):
        esperado = "autores"
        # Ejecutar la prueba
        calculado = requests.get(self.url)
        # Verificación
        assert calculado.status_code == 200
        assert calculado.json()["mensaje"]==esperado

    
    @pytest.mark.parametrize(
            ["nuevo_entrada", "esperado_entrada"],
            [({"idAutor":"02", "nombre":"Autor Pruebas", "email":"autorpruebas@gmail.com", "idPais":"MX"}, "Autor agregado con éxito"), 
            ({"idAutor":"01", "nombre":"Frank","email":"frank1996@gmail.com", "idPais":"AR"},"Id de autor ya existe")]
    )

    def test_agregar(self, nuevo_entrada,esperado_entrada):
        calculado = requests.post(self.url,json=nuevo_entrada)
        assert calculado.status_code ==200
        assert esperado_entrada == calculado.json()["mensaje"]


    
    @pytest.mark.parametrize(
            ["id_entrada","esperado_entrada"],
            [("01", "Autor encontrado"),
            ("03", "Autor no encontrado")]
    )

    def test_busqueda(self, id_entrada, esperado_entrada): 
        #La ejecucion de caso de prueba 2
        idAutor = id_entrada
        esperado = esperado_entrada
        calculado = requests.get(f"{self.url}/{idAutor}")
        #Verificacion del caso de prueba
        assert calculado.status_code==200
        assert esperado in calculado.json()["mensaje"]


    # Para cuando el usuario existe y se modifica con éxito
    def test_modifica1(self):
        idAutor = "01"
        nombre = "Frank"
        email = "frank1996@gmail.com"
        idPais = "AR"
        nuevo = {"nombre":nombre, "email":email,"idPais":idPais}
        esperado = "Autor modificado con éxito"
        # Ejecutar la prueba
        calculado = requests.put(f"{self.url}/{idAutor}",json=nuevo)
        # Verificar la prueba
        assert calculado.status_code == 200
        assert esperado in calculado.json()["mensaje"]
        sql =f"SELECT * FROM autores WHERE idAutor='{idAutor}'"
        mi_cursor.execute(sql)
        datos = mi_cursor.fetchall()[0]
        assert nombre==datos[1] and email==datos[2] and idPais==datos[3]


    # Para cuando el usuario no existe
    def test_modifica2(self):
        idAutor = "111"
        nombre = "Juan"
        email = "juanchitogamer@gmail.com"
        idPais = "MX"
        nuevo = {"nombre":nombre, "email":email, "idPais":idPais}
        esperado = "Autor no existe"
        # Ejecutar la prueba
        calculado = requests.put(f"{self.url}/{idAutor}",json=nuevo)
        # Verificar la prueba
        assert calculado.status_code == 200
        assert esperado in calculado.json()["mensaje"]

    @pytest.mark.parametrize(
        ["id_entrada","esperado_entrada"],
        [("01","Autor eliminado con éxito"),
        ("03","Autor no existe")]
    )


    def test_elimina(self,id_entrada, esperado_entrada):
        idAutor = id_entrada
        esperado = esperado_entrada
        # Ejecutar la prueba
        calculado = requests.delete(f"{self.url}/{idAutor}")
        # Verificar la prueba
        assert calculado.status_code == 200
        assert esperado in calculado.json()["mensaje"]
        mi_db.commit()
        sql =f"SELECT * FROM autores WHERE idAutor='{idAutor}'"
        mi_cursor.execute(sql)
        datos = mi_cursor.fetchall()
        assert len(datos)==0