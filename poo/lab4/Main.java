package lab4;

import java.util.Scanner;

public class Main {
    
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        // System.out.println("Digite um número em Hexadecimal ");
        // String num = input.nextLine();
        // int numero = Integer.parseInt(num, 16);
        // System.out.println(numero);

        System.out.println("Digite um número  ");
        int num = Integer.parseInt(input.nextLine());

        // String hexa = Integer.toHexString(num);

        // System.out.println(hexa);
        String bin  = Integer.toBinaryString(num);

        System.out.println(bin);
        input.close();


        
    }

}
