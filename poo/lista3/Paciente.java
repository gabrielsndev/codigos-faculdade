// Crie uma classe chamada Paciente, com os atributos peso (do tipo float) e altura (do tipo float).
// Siga as convenções de nomenclatura e visibilidade discutidas em sala de aula.


package lista3;

public class Paciente {
    private float peso;
    private float altura;

    public void setPeso(float p) {
        peso = p;
    }
    public void setAltura(float a) {
        altura =a;
    }

    public float getPeso() {
        return peso;
    }

    public float getAltura() {
        return altura;
    }

}
