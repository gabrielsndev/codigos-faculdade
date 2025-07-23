package lab7;

public  abstract class Bebida {
    private String nome;
    private double preco;
    private float teor;

    public Bebida() {};

    public void setNome(String nome) {
        this.nome = nome;
    }
    
    public void setPreco(double preco) {
        this.preco = preco;
    }
    
    public void setTeor(float teor) {
        this.teor = teor;
    }
    
    public String getNome() {
        return this.nome;
    }
    
    public double getPreco() {
        return this.preco;
    }
    
    public float getTeor() {
        return this.teor;
    }
    
    
    
}