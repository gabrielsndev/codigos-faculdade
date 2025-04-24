// Crie a classe “Triangulo”, com três atributos: lado1, lado2 e lado3, todos do tipo inteiro.
// Respeite as convenções de nomenclatura e visibilidade vistas em sala de aula.
// Adicione à classe Triangulo um método chamado tipo, que retornará um Enum correspondendo ao
// tipo do triângulo (há três tipos de triângulo: equilátero, isósceles e escaleno).
// Na matemática, um triângulo é dito equilátero se todos os seus lados têm a mesma medida;
// isósceles é quando apenas há dois lados iguais; e escaleno quando todos os lados são diferentes.
// Em Java, um Enum é um tipo especial de dado que limita os valores que uma variável pode assumir a um certo conjunto.
// Crie um Enum chamado TiposDeTriangulo, com os valores: EQUILATERO, ISOSCELES e ESCALENO.

package lista4;


public class Triangulo {
    private int lado1;
    private int lado2;
    private int lado3;

    public void setLado1(int lado) {
        lado1 = lado;
    }
    public void setLado2(int lado) {
        lado2 = lado;
    }
    public void setLado3(int lado) {
        lado3 = lado;
    }


    public int getLado1() {
        return lado1;
    }
    public int getLado2() {
        return lado2;
    }
    public int getLado3() {
        return lado3;
    }

    

    public TiposTriangulos tipo(int lado1, int lado2, int lado3){

        if (lado1 == lado2 && lado1 ==lado3) {
            return TiposTriangulos.EQUILATERO;
        }else if(lado1 == lado2 || lado1 == lado3){
            return  TiposTriangulos.ISOSCELES;
        }
        return TiposTriangulos.ESCALENO;
    }

}