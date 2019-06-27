# -*- coding: utf-8 -*-
class Usuario():
    def __init__(self, nombre, apellido, fecha_de_nacimiento, edad, direccion, telefono, github, referencia, estudio):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.github = github
        self.referencia = referencia
        self.estudio = estudio

class Estudios():
    def __init__(self, nivel, nombre_institucion, lugar, ano_inicio, ano_final):
        self.nivel = nivel
        self.nombre_institucion = nombre_institucion
        self.lugar = lugar
        self.ano_inicio = ano_inicio
        self.ano_final = ano_final
        
class Referencias():
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

referencias = [Referencias("Ines", "Solano", "3223366143"), Referencias("Odilia ", "Ardila", "3144822129"), Referencias("Sebastian", "Martinez", "3223366143")]
estudios = [Estudios("Primaria", "Gimnasio Real Americano", "Bogota", "2006", "2010"), Estudios("Secundaria", "Gimnasio Real Americano", "Bogota", "2011", "2016"), Estudios("Superior", "Universidad Distrital", "Bogota", "2017", "Actualidad")]
persona = Usuario("Kevin Andres", "Malaver Cobos", "22 - 10 - 2000", "18", "cll 51 c sur # 81i - 40", "3102338255", " https://github.com/kevinMalaver", referencias, estudios)
