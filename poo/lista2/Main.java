package lista2;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Aluno aluno = new Aluno();

        System.out.println("Diga o nome e as duas notas do aluno:");
        aluno.setNome(input.nextLine());
        aluno.setNota1(input.nextFloat());
        aluno.setNota2(input.nextFloat());

        System.out.println("A média do aluno " + aluno.getNome() + " é " + aluno.media());
        System.out.println("Agora informe o peso das notas respectivamente:");
        
        float peso1 = input.nextFloat();
        float peso2 = input.nextFloat();

        System.out.println("A média ponderada é " + aluno.mediaPonderada(peso1, peso2));

    }

}
