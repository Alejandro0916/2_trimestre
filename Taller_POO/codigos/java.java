// ==========================================
// Clase Libro
// ==========================================
public class Libro {
    // ----- ATRIBUTOS -----
    String titulo;        // Atributo que guarda el título del libro
    String autor;         // Atributo que guarda el nombre del autor
    boolean disponible;   // Atributo que indica si el libro está disponible o no

    // ----- CONSTRUCTOR -----
    // Un constructor inicializa los valores cuando se crea un objeto
    public Libro(String titulo, String autor) {
        // "this" se usa para diferenciar el atributo de la clase
        // del parámetro del constructor que se llama igual
        this.titulo = titulo;
        this.autor = autor;
        this.disponible = true; // Al inicio, el libro está disponible
    }

    // ----- MÉTODO -----
    public void mostrarLibro() {
        // "void" significa que este método no devuelve nada,
        // solo ejecuta las instrucciones dentro de las llaves {}
        System.out.println("Libro: " + titulo + " | Autor: " + autor);
    }
}

// ==========================================
// Clase Usuario
// ==========================================
public class Usuario {
    // ----- ATRIBUTOS -----
    String nombre;
    int edad;

    // ----- CONSTRUCTOR -----
    public Usuario(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    // ----- MÉTODO -----
    public void mostrarUsuario() {
        System.out.println("Usuario: " + nombre + " | Edad: " + edad);
    }
}

// ==========================================
// Clase Prestamo
// ==========================================
public class Prestamo {
    // ----- ATRIBUTOS -----
    Libro libro;
    Usuario usuario;
    String fecha;

    // ----- CONSTRUCTOR -----
    public Prestamo(Libro libro, Usuario usuario, String fecha) {
        // "this" indica que hablamos del atributo de la clase
        this.libro = libro;
        this.usuario = usuario;
        this.fecha = fecha;
        // Condición: si el libro está disponible, se presta
        if (libro.disponible == true) {
            libro.disponible = false; // el libro ya no está disponible
        }
    }

    // ----- MÉTODO -----
    public void mostrarPrestamo() {
        System.out.println("Préstamo -> Libro: " + libro.titulo +
                           " | Usuario: " + usuario.nombre +
                           " | Fecha: " + fecha);
    }
}

// ==========================================
// Clase Recepcionista
// ==========================================
public class Recepcionista {
    // ----- ATRIBUTOS -----
    String nombre;

    // ----- CONSTRUCTOR -----
    public Recepcionista(String nombre) {
        this.nombre = nombre;
    }

    // ----- MÉTODO -----
    public void mostrarRecepcionista() {
        System.out.println("Recepcionista: " + nombre);
    }
}

// ==========================================
// Clase Biblioteca
// ==========================================
public class Biblioteca {
    // ----- ATRIBUTOS -----
    String nombre;
    Recepcionista recepcionista;

    // ----- CONSTRUCTOR -----
    public Biblioteca(String nombre, Recepcionista recepcionista) {
        this.nombre = nombre;
        this.recepcionista = recepcionista;
    }

    // ----- MÉTODO -----
    public void mostrarBiblioteca() {
        System.out.println("Biblioteca: " + nombre);
        recepcionista.mostrarRecepcionista(); // muestra al recepcionista
    }
}

// ==========================================
// Clase Principal (aquí empieza el programa)
// ==========================================
public class Main {
    // "public static void main" es el punto de inicio de todo programa en Java
    // void -> no devuelve nada
    // String[] args -> son parámetros opcionales que puede recibir el programa
    public static void main(String[] args) {

        // "new" sirve para crear un objeto de una clase
        Libro l1 = new Libro("El Principito", "Antoine de Saint-Exupéry");
        Usuario u1 = new Usuario("Andres", 20);
        Recepcionista r1 = new Recepcionista("Camila");
        Biblioteca b1 = new Biblioteca("Biblioteca Central", r1);

        // Mostramos la información
        l1.mostrarLibro();        // muestra datos del libro
        u1.mostrarUsuario();      // muestra datos del usuario
        b1.mostrarBiblioteca();   // muestra info de la biblioteca y recepcionista

        // Crear un préstamo
        Prestamo p1 = new Prestamo(l1, u1, "28/08/2025");
        p1.mostrarPrestamo();
    }
}
