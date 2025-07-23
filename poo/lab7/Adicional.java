package lab7;

public abstract class Adicional extends Bebida {
    private Bebida bebida;
    
    public Adicional(Bebida b) {
        this.bebida = b;
    }
    
    public String getNome() {
        return super.getNome() + " " + bebida.getNome();
    }
    
    public double getPreco() {
        return super.getPreco() + bebida.getPreco();
    }
    
    public float getTeor() {
        return super.getTeor() + bebida.getTeor();
    }
    
    
}