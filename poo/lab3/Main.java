package lab3;
// Receba dois números e calcule a potencia do maior pelo menor
// e imprima a raiz quadrada do resultado arredondando pra cima

import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Digite um Número");
        int num1 = Integer.parseInt(input.nextLine());
        System.out.println("Digite Outro Número");
        int num2 = Integer.parseInt(input.nextLine());
        int maior;
        int menor;

        maior = Math.max(num1, num2);
        menor = Math.min(num1, num2);

        double potencia = Math.pow(maior, menor);

        System.out.println("O resultado é: " + Math.ceil(Math.sqrt(potencia)));
        

        input.close();
    }
}
