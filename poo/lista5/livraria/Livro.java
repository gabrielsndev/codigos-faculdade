package lista5.livraria;

// . Crie a classe Livro, que possuirá como atributos: título (String),
// ano de publicação (inteiro), quantidade disponível (inteiro) e preço (float).
// Essa classe representará um Livro que estará disponível para venda numa livraria.
// O atributo “quantidade disponível” indicará a quantidade desse livro que está disponível para venda
// (um livro com quantidade disponível igual a zero estaria esgotado e quando se vende um livro deve-se decrementar essa quantidade).
// Siga as convenções de nomenclatura e visibilidades estudadas em sala de aula.

// Adicione à classe Livro um método chamado eIgual.
// Ele receberá um Livro como parâmetro de entrada e devolverá um valor booleano,
// indicando se o livro recebido e o livro que está executando o método são iguais.
// Dois livros serão iguais se tiverem o mesmo título.

public class Livro {
    private String titulo;
    private int anoPublicacao;
    private int qtdDisponivel;
    private float preco; 

    public void setTitulo(String titulo){
        this.titulo = titulo;
    }

    public void setAnoPublicacao(int anoPublicacao) {
        this.anoPublicacao = anoPublicacao;
    }

    public void setQtdDisponivel(int qtd){
        qtdDisponivel = qtd;
    }

    public void setPreco(float preco) {
        this.preco = preco;
    }

    public String getTitulo(){
        return titulo;
    }

    public int getAnoPublicacao() {
        return anoPublicacao;
    }

    public float getPreco() {
        return preco;
    }

    public int getQtdDisponivel() {
        return qtdDisponivel;
    }

    
    public boolean eIgual(Livro l){
        if (l.getTitulo().equals(titulo)) {
            return true;
        }
        return false;
    }
}
