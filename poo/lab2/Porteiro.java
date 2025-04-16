// Crie uma classe chamada Porteiro. Essa classe terá um método chamado boas-vindas que dará boas vindas personalizadas.
// O retorno do método boas-vindas é uma String. Ele receberá como parâmetro de entrada um objeto do tipo Pessoa.
// O método retorna a mensagem de boas-vindas correspondente combinada com o nome da pessoa, utilizando o padrão a seguir (utilize switch case):

// Homem - Bem vindo Senhor @nome

// Mulher - Bem vinda Senhorita @nome

// Criança (se a pessoa tiver menos de 10 anos de idade – use if para esse teste) - Olá Jovem @nome

// Se a pessoa for adulta, mas o sexo não estiver atribuído – Olá @nome, tenha um ótimo dia.

package lab2;

public class Porteiro {
    
    public String boasVindas(Pessoa pessoa) {
        if (pessoa.getIdade() < 10) {
            return "Olá Jovem " + pessoa.getNome();
        }

        switch (pessoa.getSexo()){
            case "Homem":
                return "Bem vindo Senhor " + pessoa.getNome(); 
            case "Mulher":
                return "Bem vinda Senhorita " + pessoa.getNome();
            default:
                return "Olá " + pessoa.getNome() + ", tenha um ótimo dia.";
        }

    }
}
