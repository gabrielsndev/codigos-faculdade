// Crie uma classe chamada Ponto. Na matemática, um ponto é uma representação no plano cartesiano,
// onde ocorre o encontro de duas coordenadas: uma no eixo horizontal e outra no eixo vertical.

// Atributos: A classe Ponto deverá possuir dois atributos, representando as coordenadas, sendo eles:

// x: Coordenada no eixo horizontal (do tipo inteiro).
// y: Coordenada no eixo vertical (do tipo inteiro).

// Encapsulamento: Respeite as convenções de nomenclatura e visibilidade, como discutido em sala de aula.
// Ou seja, é necessário criar os métodos getters e setters para acessar e modificar esses atributos.

package lista3.questao2;

public class Ponto {
    private int eixoX;
    private int eixoY;

    public void setEixoX(int x){
        eixoX = x;
    }
    public void setEixoY(int y) {
        eixoY = y;
    }

    public int getEixoX(){
        return eixoX;
    }
    public int getEixoY() {
        return eixoY;
    }


    
}
