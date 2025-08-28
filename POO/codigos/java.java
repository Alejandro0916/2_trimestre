// =============================================================
// Clase Libro
public class Libro {

    // Atributos (datos del libro)
    String titulo;
    String autor;
    String isbn;
    int anio_publicacion;
    boolean prestado;

    // Constructor (sirve para crear el libro)
    public Libro(String t, String a, String i, int anio) {
        titulo = t;
        autor = a;
        isbn = i;
        anio_publicacion = anio;
        prestado = false;   // al inicio el libro no está prestado
    }

    // Método para prestar el libro
    public void prestar() {
        prestado = true;
        System.out.println("El libro '" + titulo + "' ha sido prestado.");
    }

    // Método para devolver el libro
    public void devolver() {
        prestado = false;
        System.out.println("El libro '" + titulo + "' ha sido devuelto.");
    }
}


// =============================================================
// Clase Usuario
public class Usuario {

    // Atributos
    String nombre;
    String correo;
    int id;

    // Constructor
    public Usuario(String n, String c, int i) {
        nombre = n;
        correo = c;
        id = i;
    }

    // Método para mostrar la información del usuario
    public void mostrarUsuario() {
        System.out.println("Usuario: " + nombre + ", correo: " + correo + ", id: " + id);
    }
}


// =============================================================
// Clase Biblioteca
public class Biblioteca {

    // Atributos
    String nombre;
    Libro libro1;   // solo guardamos 1 libro para que sea fácil
    Libro libro2;   // otro libro (máximo 2)

    // Constructor
    public Biblioteca(String n) {
        nombre = n;
    }

    // Método para agregar libros
    public void agregarLibros(Libro l1, Libro l2) {
        libro1 = l1;
        libro2 = l2;
        System.out.println("Se agregaron 2 libros a la biblioteca '" + nombre + "'");
    }

    // Método para mostrar los libros
    public void mostrarLibros() {
        System.out.println("Libros en la biblioteca '" + nombre + "':");
        System.out.println("- " + libro1.titulo + " de " + libro1.autor);
        System.out.println("- " + libro2.titulo + " de " + libro2.autor);
    }
}


// =============================================================
// Clase principal (donde corre el programa)
public class Main {
    public static void main(String[] args) {

        // Crear biblioteca
        Biblioteca biblio = new Biblioteca("Central");

        // Crear libros
        Libro l1 = new Libro("Cien años de soledad", "Gabriel García Márquez", "12345", 1967);
        Libro l2 = new Libro("El Principito", "Antoine de Saint-Exupéry", "67890", 1943);

        // Agregar los libros a la biblioteca
        biblio.agregarLibros(l1, l2);

        // Mostrar los libros
        biblio.mostrarLibros();

        // Crear un usuario
        Usuario u1 = new Usuario("Alejandro", "alejandro@mail.com", 1);
        u1.mostrarUsuario();

        // Prestar y devolver un libro
        l1.prestar();
        l1.devolver();
    }
}
