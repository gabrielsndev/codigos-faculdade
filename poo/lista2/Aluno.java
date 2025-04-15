package lista2;


// Crie uma classe chamada Aluno. Aluno terá como atributos um nome (String) e duas notas (float), como atributos.
// Siga as convenções de nomenclatura e visibilidade que estudamos.
// Adicione à classe Aluno um método chamado media, que não terá parâmetros de entrada e retornará um valor float.
// Esse método retornará a média das duas notas que são atributos do Aluno.
// Adicione à classe Aluno outro método chamado média ponderada, que receberá dois valores float
// (correspondentes ao peso de cada nota do Aluno). O método da média ponderada retorna o resultado do seguinte cálculo:
// peso1 * nota1 + peso2 * nota2
// Escreva um programa onde você vai ler os dados de um aluno. Depois, crie um objeto aluno
// e exiba o nome dele seguido da média das suas notas. Depois leia o peso de cada uma das notas
// e exiba o resultado do método média ponderada.


public class Aluno {
    private String nome;
    private float nota1;
    private float nota2;

    public String getNome() {
        return nome;
    }
    public float getNota1() {
        return nota1;
    }
    public float getNota2() {
        return nota2;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
    public void setNota1(float nota) {
        this.nota1 = nota;
    }
    public void setNota2(float nota) {
        this.nota2 = nota;
    }

    public float media(){
        return (nota1 + nota2) / 2;
    }

    public float mediaPonderada(float peso1, float peso2){
        return peso1 * nota1 + peso2 * nota2;
    }

}