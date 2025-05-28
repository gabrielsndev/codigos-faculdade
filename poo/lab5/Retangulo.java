package lab5;

public class Retangulo extends FormaGeometrica{

    public Retangulo(double base, double altura) {
        this.base = base;
        this.altura= altura;
    }


    private double base;
    private double altura;


    public double getAltura() {
        return altura;
    }

    public double getBase() {
        return base;
    }


    public void setAltura(double altura) {
        this.altura = altura;
    }

    public void setBase(double base) {
        this.base = base;
    }


    public double calculoArea() {
        return base * altura;
    }

    public double calculoPerimetro() {
        return 2 * (base + altura);
    }

    
}
