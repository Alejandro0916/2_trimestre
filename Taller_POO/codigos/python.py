#CODIGO DE PYHON DEL PUNTO 11 - 15

# ==========================
# CLASES DE LA BIBLIOTECA
# ==========================

# --------- Clase Autor ---------
class Autor:
#Clase que representa a un autor de libros.
    def __init__(self, nombre, nacionalidad, fecha_nacimiento):
        self.nombre = nombre               # ATRIBUTO: almacena el nombre del autor
        self.nacionalidad = nacionalidad   # ATRIBUTO: almacena la nacionalidad del autor
        self.fecha_nacimiento = fecha_nacimiento  # ATRIBUTO: almacena la fecha de nacimiento

    def mostrar_info(self):
        # MÉTODO: imprime la información del autor
        print("Autor:", self.nombre, "- Nacionalidad:", self.nacionalidad, "- Nacimiento:", self.fecha_nacimiento)
# --------- Clase Libro ---------
class Libro:
#Clase que representa un libro de la biblioteca.
    def __init__(self, titulo, autor, isbn, genero, año_publicacion):
        self.titulo = titulo              # ATRIBUTO: título del libro
        self.autor = autor                # ATRIBUTO: objeto Autor que escribió el libro
        self.isbn = isbn                  # ATRIBUTO: código único ISBN
        self.genero = genero              # ATRIBUTO: género literario
        self.año_publicacion = año_publicacion  # ATRIBUTO: año de publicación
        self.disponible = True            # ATRIBUTO: indica si el libro está disponible para préstamo

    def mostrar_info(self):
        # MÉTODO: imprime toda la información del libro, incluyendo disponibilidad
        print("Título:", self.titulo, "- Autor:", self.autor.nombre, "- ISBN:", self.isbn,
              "- Género:", self.genero, "- Año:", self.año_publicacion, "- Disponible:", self.disponible)
# --------- Clase Usuario ---------
class Usuario:
#Clase que representa un usuario de la biblioteca.
    def __init__(self, nombre, id_usuario, edad, email):
        self.nombre = nombre               # ATRIBUTO: nombre del usuario
        self.id_usuario = id_usuario       # ATRIBUTO: ID único del usuario
        self.edad = edad                   # ATRIBUTO: edad del usuario
        self.email = email                 # ATRIBUTO: correo electrónico del usuario

        # ATRIBUTOS: libros que tiene prestados. Inicialmente no tiene ninguno, por eso usamos None
        self.prestamo1 = None
        self.prestamo2 = None

        # EXPLICACIÓN DE None:
        # None significa “no tiene valor todavía” o “vacío”.
        # Se usa aquí porque el usuario aún no ha recibido ningún libro.
        # Esto evita errores si intentamos acceder a atributos de un libro que todavía no existe.

    def mostrar_usuario(self):
        # MÉTODO: imprime información del usuario y sus libros
        print("Usuario:", self.nombre, "- ID:", self.id_usuario, "- Edad:", self.edad, "- Email:", self.email)
        print("Libros prestados:")

        # if self.prestamo1 is not None:
        # VERIFICACIÓN: 'is not None' significa “si prestamo1 tiene un libro asignado”
        # Si prestamo1 es None, no imprime nada para evitar error
        if self.prestamo1 is not None:
            print("-", self.prestamo1.titulo)  # Solo imprime si hay un libro

        # Igual para prestamo2
        if self.prestamo2 is not None:
            print("-", self.prestamo2.titulo)  # Solo imprime si hay un libro
# --------- Clase Prestamo ---------
class Prestamo:
# Clase que representa un préstamo de libro a un usuario.
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.libro = libro                      # ATRIBUTO: libro que se presta
        self.usuario = usuario                  # ATRIBUTO: usuario que recibe el libro
        self.fecha_prestamo = fecha_prestamo    # ATRIBUTO: fecha del préstamo
        self.fecha_devolucion = fecha_devolucion# ATRIBUTO: fecha límite para devolver el libro

    def mostrar_prestamo(self):
        # MÉTODO: imprime los detalles del préstamo
        print("Libro:", self.libro.titulo, "- Prestado a:", self.usuario.nombre,
              "- Fecha de préstamo:", self.fecha_prestamo, "- Fecha de devolución:", self.fecha_devolucion)
# --------- Clase Recepcionista ---------
class Recepcionista:
#    Clase que representa un recepcionista de la biblioteca.

    def __init__(self, nombre, id_empleado):
        self.nombre = nombre             # ATRIBUTO: nombre del recepcionista
        self.id_empleado = id_empleado   # ATRIBUTO: ID del empleado

    def registrar_usuario(self, biblioteca, usuario):
        # MÉTODO: registra un usuario en la biblioteca
        biblioteca.usuario1 = usuario
        print("Usuario", usuario.nombre, "registrado por", self.nombre)

    def prestar_libro(self, biblioteca, usuario, libro, fecha_prestamo, fecha_devolucion):

#  MÉTODO: presta un libro a un usuario solo si está disponible.
#         BLOQUE IF/ELSE:
#         - if libro.disponible: solo se ejecuta si el libro está disponible (True)
#             - Crea un objeto Prestamo
#             - Asigna el libro al usuario
#             - Cambia disponible = False
#             - Imprime mensaje de préstamo exitoso
#         - else: se ejecuta si libro.disponible es False
#             - Imprime que el libro no se puede prestar
        if libro.disponible:  # Comienza el bloque de condición
            prestamo = Prestamo(libro, usuario, fecha_prestamo, fecha_devolucion)  # CREAR PRÉSTAMO
            usuario.prestamo1 = libro     # ASIGNAR libro al usuario
            libro.disponible = False      # MARCAR libro como no disponible
            print("Libro", libro.titulo, "prestado a", usuario.nombre, "por", self.nombre)
        else:  # Bloque ELSE: se ejecuta si el libro NO está disponible
            print("El libro", libro.titulo, "no está disponible para préstamo")
# --------- Clase Biblioteca ---------
class Biblioteca:
#Clase que representa una biblioteca.
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre        # ATRIBUTO: nombre de la biblioteca
        self.direccion = direccion  # ATRIBUTO: dirección
        self.telefono = telefono    # ATRIBUTO: teléfono
        self.libro1 = None          # ATRIBUTO: primer libro registrado (None indica que aún no hay libro)
        self.usuario1 = None        # ATRIBUTO: primer usuario registrado (None indica que aún no hay usuario)
        self.prestamo1 = None       # ATRIBUTO: primer préstamo registrado (None indica que aún no hay préstamo)

    def agregar_libro(self, libro):
        # MÉTODO: agrega un libro a la biblioteca
        self.libro1 = libro
        print("Libro", libro.titulo, "agregado a la biblioteca", self.nombre)


# ==========================
# BLOQUE PRINCIPAL
# ==========================
# Aquí comienza la ejecución del programa real

# Crear autores
autor1 = Autor("Gabriel García Márquez", "Colombiano", "06/03/1927")
autor2 = Autor("Antoine de Saint-Exupéry", "Francés", "29/06/1900")

# Crear libros
libro1 = Libro("Cien Años de Soledad", autor1, "111", "Novela", 1967)
libro2 = Libro("El Principito", autor2, "222", "Fábula", 1943)

# Crear biblioteca
mi_biblioteca = Biblioteca("Biblioteca Central", "Calle 123", "555-1234")
mi_biblioteca.agregar_libro(libro1)
mi_biblioteca.agregar_libro(libro2)

# Crear usuarios
usuario1 = Usuario("Alejandro", "U1", 20, "alejandro@mail.com")  # prestamo1 y prestamo2 = None
usuario2 = Usuario("Andrés", "U2", 22, "andres@mail.com")        # prestamo1 y prestamo2 = None

# Crear recepcionista
recepcionista = Recepcionista("Marta", "R1")
recepcionista.registrar_usuario(mi_biblioteca, usuario1)
recepcionista.registrar_usuario(mi_biblioteca, usuario2)

# Prestar libros usando el if para disponibilidad
recepcionista.prestar_libro(mi_biblioteca, usuario1, libro1, "01/09/2025", "10/09/2025")  # True -> se presta
recepcionista.prestar_libro(mi_biblioteca, usuario2, libro1, "02/09/2025", "12/09/2025")  # False -> mensaje
recepcionista.prestar_libro(mi_biblioteca, usuario2, libro2, "02/09/2025", "12/09/2025")  # True -> se presta

# Mostrar información de usuarios
usuario1.mostrar_usuario()
usuario2.mostrar_usuario()