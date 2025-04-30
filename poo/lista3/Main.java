// Escreva um programa em que você lerá os dados de um paciente e usará o nutricionista para exibir qual
// a classificação do paciente.
package lista3;
import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Digite seu peso e altura respectivamente");
        Paciente paciente = new Paciente();
        Nutricionista nutricionista = new Nutricionista();

        paciente.setPeso(Float.parseFloat(input.nextLine()));
        paciente.setAltura(Float.parseFloat(input.nextLine()));

        System.err.println(nutricionista.calcularImc(paciente));
        input.close();
    }
}

