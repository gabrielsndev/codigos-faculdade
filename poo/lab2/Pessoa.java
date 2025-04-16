// Crie uma classe chamada Pessoa com os seguintes atributos: nome (String), sexo (String), peso (float), altura (int – pois é em centímetros), idade (int).
// Siga as convenções de nomenclatura de visibilidade vistas em sala de aulas e crie os gets e sets correspondentes.

package lab2;

public class Pessoa {
    private String nome;
    private String sexo;
    private float peso;
    private int altura;
    private int idade;

    public String getNome() {
        return nome;
    }
    public String getSexo() {
        return sexo;
    }
    public float getPeso() {
        return peso;
    }
    public int getAltura() {
        return altura;
    }
    public int getIdade() {
        return idade;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public void setSexo(String sexo) {
        this.sexo = sexo;
    }
    public void setPeso(float peso) {
        this.peso = peso;
    }
    public void setAltura(int altura) {
        this.altura = altura;
    }
    public void setIdade(int idade) {
        this.idade = idade;
    }


    
}