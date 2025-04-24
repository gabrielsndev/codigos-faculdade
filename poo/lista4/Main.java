package lista4;

// Escreva um programa que leia os dados referentes a uma quantidade indeterminada de triângulos.

import java.util.Scanner;

// Após ler os dados de um triângulo, pergunte ao usuário se ele deseja fornecer os dados de um novo triângulo ou encerrar o programa.
// Antes de encerrar o programa, informe a quantidade de triângulos de cada tipo lidos.
// Essa contagem deve ser feita durante o processo de leitura de cada triângulo.


public class Main {

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int isosceles = 0;
        int equilatero = 0; 
        int escaleno = 0;

        boolean condicao = true;

        do { 
            System.out.println("Digite o primeiro lado de um triângulo:");
            int lado1 = Integer.parseInt(input.nextLine());
            System.out.println("Digite o segundo lado de um triângulo:");
            int lado2 = Integer.parseInt(input.nextLine());
            System.out.println("Digite o terceiro lado de um triângulo:");
            int lado3 = Integer.parseInt(input.nextLine());

            Triangulo triangulo  = new Triangulo();
            TiposTriangulos tipo = triangulo.tipo(lado1, lado2, lado3);

            System.out.println(tipo);

            switch (tipo) {
                case EQUILATERO:
                    equilatero++;
                    break;
                case  ISOSCELES:
                    isosceles++;
                    break;
                case ESCALENO:
                    escaleno++;
                    break;
                default:
                    System.out.println("Caso inválido");
                    break;
            }

            System.out.println("Digite 1 para continuar adicionando triângulos ou 0 para encerrar o programa");
            int desejo = Integer.parseInt(input.nextLine());
                if (desejo == 0){
                    condicao = false;
                }else{
                    condicao = true;
                }

        } while (condicao);
        
        System.out.println("O número de Triângulos Escalenos é " + escaleno);
        System.out.println("O número de Triângulos Equiláteros é " + equilatero);
        System.out.println("O número de Triângulos Isosceles é " + isosceles);

        input.close();
    }
}
