package lista5.livraria;

// Crie a classe Livraria. Essa classe servirá para organizar o estoque
// (livros disponíveis para venda) e o caixa da Livraria. Adicione à classe Livraria,
// como atributo, um array de Livro, com capacidade para armazenar 100 livros.
// Além disso, inclua também um atributo chamado “quantidade de livros cadastrados”
// (esse atributo guardará a quantidade de objetos que estão “guardados” no array
// – mesmo se a quantidade disponível de um livro for 10 exemplares, ele contará como um único objeto “guardado”).
// Por fim, a Livraria terá um atributo do tipo float chamado “saldo em caixa”,
// que guardará o total acumulado com as vendas da livraria (começa com o valor zero, assim como a quantidade de livros cadastrados).
// Siga as convenções de nomenclatura e visibilidade vistas em sala de aula, entretanto,
// crie apenas os métodos gets para os atributos
// (a única forma de mudar os valores dos atributos será através dos métodos da Livraria que você programará nas próximas questões).

// Adicione à classe Livraria um método chamado “cadastrar livro”,
// que receberá como parâmetro de entrada um objeto do tipo Livro e retornará um valor booleano.
// O método “salva” o Livro recebido na próxima posição disponível do vetor de Livros. Entretanto,
// não deve ser permitido cadastrar Livros iguais no vetor (ou seja, livros com o mesmo título).
// O método retorna verdadeiro, se o cadastro foi bem sucedido, ou falso, caso contrário. Após adicionar o Livro,
// lembre-se de atualizar o atributo “quantidade de livros cadastrados” da classe Livraria.

// Adicione à classe Livraria um método chamado “comprar livro”, que receberá uma String,
// que representa o título do Livro, como parâmetro de entrada e retornará uma String,
// que representará o resultado da tentativa de compra. O método comprar livro irá procurar, no vetor,
// um Livro com o mesmo título que o recebido como parâmetro de entrada.
// Caso seja encontrado um livro e ele esteja disponível para venda (há quantidade disponível),
// o método atualiza a quantidade disponível daquele título, atualiza o caixa da Livraria (para incluir o valor do livro vendido)
// e retorna a String “SUCESSO”. Caso seja encontrado um livro, mas não haja quantidade disponível para venda,
// o método retorna a String “ESGOTADO”.
// Caso não seja encontrado um livro, o método retorna “NÃO ENCONTRADO”.



public class Livraria {
    private Livro[] estoque = new Livro[100];
    private int qtdLivrosCadastrados = 0;
    private float saldoCaixa = 0;

    public Livro[] getEstoque() {
        return estoque;
    }

    public int getQtdlivrosCadastrados() {
        return qtdLivrosCadastrados;
    }

    public float getSaldoCaixa() {
        return saldoCaixa;
    }


    public boolean cadastrarLivro(Livro l) {
        for(int i = 0; i != qtdLivrosCadastrados; i++ ){
            if (estoque[i].eIgual(l)) {
                return false;
            }
        }
        estoque[qtdLivrosCadastrados] = l;
        qtdLivrosCadastrados++;
        return true;
    }

    public String comprarLivro(String livro){
        for (Livro book : estoque) {
            if (book.getTitulo().equals(livro)) {
                if (book.getQtdDisponivel() > 0) {
                    book.setQtdDisponivel(book.getQtdDisponivel() - 1);
                    saldoCaixa += book.getPreco();
                    return "SUCESSO";
                }
                else{
                    return "ESGOTADO";
                }
            }
        }
        return "NÃO ENCONTRADO";
    }
}
