package lab5;

public class Triangulo extends FormaGeometrica {

    public Triangulo(double ladoa, double ladob, double ladoc) {
        this.lado1 = ladoa; 
        this.lado2 = ladob;
        this.lado3 = ladoc;
    }

    double lado1;
    double lado2;
    double lado3;


    public double calculoArea() {
        double s = (lado1 + lado2 + lado3) / 2.0; // semiperímetro
        return Math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3));
    }

    public double calculoPerimetro() {
        return lado1 + lado2 + lado3;
    }
    
    
}
