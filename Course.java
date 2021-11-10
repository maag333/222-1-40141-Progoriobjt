public class Course {
    public String nombre_materia;
    public int codigo;
    public String programa;
    public int numero_alumnos;
    public String docente;
    public int numero_de_examen;

    public Course(String nombre_materia, int codigo, String programa, int numero_alumnos, String docente, int numero_de_examen){
        super();
        this.nombre_materia = nombre_materia;
        this.codigo = codigo;
        this.programa = programa;
        this.numero_alumnos = numero_alumnos;
        this.docente =docente;
        this.numero_de_examen = numero_de_examen;
    }
    
    public String datos_curso(String nombre_materia, String programa, int codigo){
        return nombre_materia+" es del programa "+programa+" con numero de codigo "+codigo;
    }

    public int lista_definitiva(int numero_alumnos){
        return numero_alumnos+3;
    }
    
    public static void Proceso_terminado(){
        System.out.println("Tarea Finalizada");
    }

    public void nota_prueba(){
        System.out.println("Este algoritmo es solo un demo");
    }

    public static void alumno_examen(){
        System.out.println("Este Examen fue realizado por Mario Alcocer");
    }

}
