package lab5;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Digite a quantidade de formas que deseja definir: ");
        int qtdFormas = Integer.parseInt(input.nextLine());

        int qtdCirculo = 0;
        int qtdRetangulo = 0;
        int qtdTriangulo = 0;


        ArrayList<Triangulo> arrayTriangulo = new ArrayList<>();
        ArrayList<Circulo> arrayCirculo = new ArrayList<>();
        ArrayList<Retangulo> arrayRetangulo = new ArrayList<>();

        for(int i = 1; i <= qtdFormas; i++) {
            System.out.println("Que forma deseja criar: ");
            String forma = input.nextLine();
            switch (forma) {
                case "triangulo":
                    System.out.println("Digite as medidas dos 3 lados");
                    Triangulo triangulo = new Triangulo(Integer.parseInt(input.nextLine()), Integer.parseInt(input.nextLine()), Integer.parseInt(input.nextLine()));
                    arrayTriangulo.add(triangulo);
                    qtdTriangulo++;
                    break;

                case  "retangulo":
                    System.out.println("Digite a base, depois a altura");
                    Retangulo retangulo = new Retangulo(Integer.parseInt(input.nextLine()), Integer.parseInt(input.nextLine()));
                    arrayRetangulo.add(retangulo);
                    qtdRetangulo++;
                    break;

                case  "circulo":
                    System.out.println("Digite o raio do circulo");
                    Circulo circulo = new Circulo(Integer.parseInt(input.nextLine()));
                    arrayCirculo.add(circulo);
                    qtdCirculo++;

            }
        }

        for (Retangulo retangulo : arrayRetangulo) {
            System.out.println("Área: " + retangulo.calculoArea() + " Perímetro: " + retangulo.calculoPerimetro());
        }

        for (Circulo circulo : arrayCirculo) {
            System.out.println("Área: " + circulo.calculoArea() + " Perímetro: " + circulo.calculoPerimetro());
        }
        for (Triangulo triangulo: arrayTriangulo) {
            System.out.println("Área: " + triangulo.calculoArea() + " Perímetro: " + triangulo.calculoPerimetro());
            
        }
    }
}
