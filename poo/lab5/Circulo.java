package lab5;

public class Circulo extends FormaGeometrica {

    public Circulo(double raio) {
        this.raio = raio;
    }

    private double raio;

    public double getRaio() {
        return raio;
    }

    public void setRaio(double raio) {
        this.raio = raio;
    }

    public double calculoArea(){
        return Math.PI * Math.pow(raio, 2);
    }

    public double calculoPerimetro() {
        return 2 * Math.PI * raio;
    }
}
