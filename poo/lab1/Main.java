package lab1;

import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Digite o nome do produto: ");

		ProdutoImportado produto = new ProdutoImportado();
		produto.setNomeProduto(input.nextLine()); 

		System.out.println("Digite o preço do produto: ");
		produto.setPrecoProduto(input.nextFloat());
		
		System.out.println("Qual a cotação atual do real? ");
		System.out.println("A cotação atual é : " + produto.getPrecoConvertido(input.nextFloat()));
	}
}
