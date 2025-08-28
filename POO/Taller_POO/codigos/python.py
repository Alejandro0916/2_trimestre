# -------------------------------
# CLASE AUTOR
# -------------------------------
class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento, bibliografia):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.bibliografia = bibliografia

    def mostrar_info(self):
        print(f"Autor: {self.nombre}, Nacionalidad: {self.nacionalidad}")

    def listar_libros(self):
        print(f"Libros de {self.nombre}: {self.bibliografia}")


# -------------------------------
# CLASE LIBRO
# -------------------------------
class Libro:
    def __init__(self, titulo, autor, ISBN, genero, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.genero = genero
        self.año_publicacion = año_publicacion
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"📖 '{self.titulo}' ha sido prestado.")
        else:
            print(f"⚠ '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"✅ '{self.titulo}' ha sido devuelto.")

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"{self.titulo} ({self.año_publicacion}) - {self.autor} | {estado}")


# -------------------------------
# CLASE USUARIO
# -------------------------------
class Usuario:
    def __init__(self, nombre, id_usuario, direccion, telefono):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.direccion = direccion
        self.telefono = telefono

    def solicitar_prestamo(self, libro):
        print(f"{self.nombre} solicita '{libro.titulo}'...")
        libro.prestar()

    def devolver_libro(self, libro):
        print(f"{self.nombre} devuelve '{libro.titulo}'...")
        libro.devolver()

    def consultar_libro(self, libro):
        print(f"{self.nombre} consulta el libro:")
        libro.mostrar_info()


# -------------------------------
# CLASE PRESTAMO
# -------------------------------
class Prestamo:
    def __init__(self, id_prestamo, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.id_prestamo = id_prestamo
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def registro_prestamo(self):
        print(f"📌 Préstamo {self.id_prestamo}: {self.usuario.nombre} tiene '{self.libro.titulo}'")

    def finalizar_prestamo(self):
        print(f"✅ Préstamo {self.id_prestamo} finalizado.")
        self.libro.devolver()

    def calcular_multa(self):
        print("💰 Multa calculada (ejemplo, no hay cálculo real).")


# -------------------------------
# CLASE RECEPCIONISTA
# -------------------------------
class Recepcionista:
    def __init__(self, nombre, id_empleado, turno):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.turno = turno

    def registrar_usuario(self, usuario):
        print(f"Recepcionista {self.nombre} registró al usuario {usuario.nombre}")

    def registrar_libro(self, libro):
        print(f"Recepcionista {self.nombre} registró el libro '{libro.titulo}'")

    def gestionar_prestamo(self, prestamo):
        prestamo.registro_prestamo()

    def gestionar_devolucion(self, prestamo):
        prestamo.finalizar_prestamo()


# -------------------------------
# CLASE BIBLIOTECA
# -------------------------------
class Biblioteca:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    def agregar_libro(self, libro):
        print(f"📚 Libro '{libro.titulo}' agregado a la biblioteca {self.nombre}")

    def eliminar_libro(self, libro):
        print(f"🗑 Libro '{libro.titulo}' eliminado de la biblioteca {self.nombre}")

    def buscar_libro(self, libro):
        print(f"🔎 Libro encontrado: {libro.titulo}")

    def mostrar_catalogo(self):
        print(f"📖 Mostrando catálogo de la biblioteca {self.nombre}")
