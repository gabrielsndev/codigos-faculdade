package lab1;

/*
Projeto Compras Internacionais
1. Crie uma classe chamada Produto Importado. Ela terá como atributos o nome do produto (String) e o preço em dólar (float).
2. Adicione ao Produto Importado um método chamado getPrecoConvertido, o qual receberá como parâmetro
de entrada um valor float correspondente a cotação da moeda que se deseja converter. Esse método retorna
o preço do p
roduto importado “convertido” para esta moeda (é só multiplicar a cotação pelo preço em dólar).
3. Escreva um programa onde você vai criar um objeto Produto Importado. Pergunte o nome do produto
importado e o preço em dólar ao usuário. Em seguida, pergunt
e ao usuário a cotação atual do real (isto é,quantos reais equivalem a um dólar)
e use o retorno do método getPrecoConvertido para exibir para o usuário
o preço do Produto Importado convertido para reais*/

public class ProdutoImportado {
	private String nomeProduto;
	private float precoProduto;
	
	public String getNomeProduto() {
		return nomeProduto;
	}
	
	public void setNomeProduto(String x) {
		nomeProduto = x;
	}
	
	public float getprecoProduto() {
		return precoProduto;
	}
	
	public void setPrecoProduto(float x) {
		precoProduto = x;
	}
	
	public float getPrecoConvertido(float cotacao) {
		return precoProduto * cotacao;
	}
}
