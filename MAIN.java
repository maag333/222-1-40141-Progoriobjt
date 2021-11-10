public class MAIN {

    public static void main(String[] args){
        Course MD = new Course("Matematicas Discretas", 42590, "semiescolarizado", 8, "Miguel Pasillas",2);
        Course DW = new Course("Desarrollo Web", 31339, "escolarizado", 20, "Ricardo Tovar",1);
        Course MB = new Course("Matematicas Basicas", 11111, "impulso", 6, "Nestor Padilla",3);

        System.out.println(MD.datos_curso(MD.nombre_materia, MD.programa, MD.codigo));
        System.out.println("El total de alumnos en la lista definitiva de la materia "+DW.nombre_materia+" es de: "+DW.lista_definitiva(DW.numero_alumnos));
        System.out.println("La materia: " + MB.nombre_materia + ", tiene como codigo de materia: " + MB.codigo + " y es del programa: " + MB.programa);


        Course.Proceso_terminado();
        DW.nota_prueba();
        Course.alumno_examen();
    }
    
}