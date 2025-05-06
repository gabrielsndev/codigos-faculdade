package lista5;

import java.util.Scanner;

// Crie um programa onde você receberá uma sequência de números separados por vírgula e, ao final,
// informará qual dos números é o maior e qual é o menor.
// Para fazer essa leitura, você deve ler a linha inteira como uma String e “quebrar” essa entrada em várias,
// usando um dos métodos de String (pesquise qual método faz isso).
// Para identificar o maior e o menor, faça uso do método max e min da classe Math.


// Escreva um programa onde você receberá do usuário uma entrada no formato de String e,
// ao final, informará quantas vogais e quantas consoantes a entrada possuía (ignore a possibilidade de vogais com acento).
// Pesquise como caracterizar um caractere como vogal ou consoante.




public class Main {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        // String numeros = input.nextLine();

        // String[] numeroStrings = numeros.split(",");

        // int maior = Integer.MIN_VALUE;
        // int menor = Integer.MAX_VALUE;

        // for (String numeroTexto : numeroStrings) {
        //     int numero = Integer.parseInt(numeroTexto.trim());
        //     if (numero > maior) {
        //         maior = numero;
        //     }
        //     if (numero < menor) {
        //         menor = numero;
        //     }
        // }

        // System.out.println("O maior número lido foi: " + maior);
        // System.out.println("O menor número lido foi: " + menor);


        System.out.println("Digite uma palavra: ");
        String entrada = input.nextLine();
        int vogal = 0;
        int consoante = 0;

        for(int i = 0; i != entrada.length(); i++){
            char letter = entrada.charAt(i);
            if ( letter == 'a' || letter == 'e' || letter =='i' || letter == 'o' || letter == 'u') {
                vogal++;
            } else {
                consoante++;
            }
        }

        System.out.println("A quantidade de vogais é: " + vogal);
        System.out.println("A quantidade de consoantes é: " + consoante);


        input.close();
    }

    
    
}
