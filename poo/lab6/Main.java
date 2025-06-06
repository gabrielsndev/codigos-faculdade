package lab6;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Random rand = new Random();
        Scanner input = new Scanner(System.in);
        System.out.println("Digite o nome do primeiro jogador:");
        String jogador1 = input.nextLine();
        System.out.println("Digite o nome do segundo jogador:");
        String jogador2 = input.nextLine();
        int carteira1 = 500;
        int carteira2 = 500;
        ArrayList<Unidade> tropas1 = new ArrayList<>();
        ArrayList<Unidade> tropas2 = new ArrayList<>();

        

        while(carteira1 >= 50) {
            System.out.println("-------------");
            System.out.println("Valores e tropas a serem escolhidas:");
            System.out.println("Catapulta - 200");
            System.out.println("Cavalaria - 100");
            System.out.println("Infantaria - 50");
            System.out.println("-------------");
            System.out.println("Digite a tropa escolhida");
            String escolha = input.nextLine();
            switch (escolha) {
                case "infantaria":
                    if(carteira1 >= 50) {
                        Infantaria infantaria = new Infantaria();
                        tropas1.add(infantaria);
                        System.out.println("Tropa adicionada com sucesso");
                        carteira1 -= 50;
                    } else {
                        System.out.println("Impossível comprar essa tropa");
                    }
                    break;
                    
                case "Cavalaria":
                    if( carteira1 >= 100) {
                        Cavalaria cavalaria = new Cavalaria();
                        tropas1.add(cavalaria);
                        System.out.println("Tropa adicionada com sucesso");
                        carteira1 -= 100;
                    } else {
                        System.out.println("Impossível comprar essa tropa");
                    }
                    break;
                
                case "Catapulta":
                    if( carteira1 >= 200) {
                        Catapulta catapulta = new Catapulta();
                        tropas1.add(catapulta);
                        System.out.println("Tropa adicionada com sucesso");
                        carteira1 -= 200;
                    } else {
                        System.out.println("Impossível comprar essa tropa");
                    }
                    break;

                default:
                    System.out.println("Tropa inválida");
                    break;
            }
        }
        System.out.println("Jogador " + jogador1 + " esgotou sua carteira:");

        System.out.println("Vez do jogador " + jogador2 + " escolher as tropas:");
        while(carteira2 >= 50) {
            System.out.println("-------------");
            System.out.println("Valores e tropas a serem escolhidas:");
            System.out.println("Catapulta - 200");
            System.out.println("Cavalaria - 100");
            System.out.println("Infantaria - 50");
            System.out.println("-------------");
            System.out.println("Digite a tropa escolhida");
            String escolha = input.nextLine();
            switch (escolha) {
                case "Infantaria":
                    if(carteira2 >= 50) {
                        Infantaria infantaria = new Infantaria();
                        tropas2.add(infantaria);
                        System.out.println("Tropa adicionada com sucesso");
                        carteira2 -= 50;
                    } else {
                        System.out.println("Impossível comprar essa tropa");
                    }
                    break;
                    
                case "Cavalaria":
                    if( carteira2 >= 100) {
                        Cavalaria cavalaria = new Cavalaria();
                        tropas2.add(cavalaria);
                        System.out.println("Tropa adicionada com sucesso");
                        carteira2 -= 100;
                    } else {
                        System.out.println("Impossível comprar essa tropa");
                    }
                    break;
                
                case "Catapulta":
                    if( carteira2 >= 200) {
                        Catapulta catapulta = new Catapulta();
                        tropas2.add(catapulta);
                        System.out.println("Tropa adicionada com sucesso");
                        carteira2 -= 200;
                    } else {
                        System.out.println("Impossível comprar essa tropa");
                    }
                    break;

                default:
                    System.out.println("Tropa inválida");
                    break;
            }
        }


    System.out.println("O jogo vai começar");

    while(!tropas1.isEmpty() && !tropas2.isEmpty()) {
        int indiceAleatorio1 = rand.nextInt(tropas1.size());
        int indiceAleatorio2 = rand.nextInt(tropas2.size());

        Unidade unidade1 = tropas1.get(indiceAleatorio1);
        Unidade unidade2 = tropas2.get(indiceAleatorio2);

        System.out.println("Unidades a batalhar: " + unidade1.toString() + " " + unidade2.toString());

        if(unidade1.ganharQuandoAtacadoPor(unidade2)) {
            System.out.println("Unidade vencedora " + unidade1.toString() + ".  Unidade perdedora " + unidade2.toString());
            unidade2.receberDano();
            if(unidade2.isVivo()) {
                System.out.println("Continua viva");
            } else {
                System.out.println("Morreu");
                tropas2.remove(indiceAleatorio2);
            }
        }
        else if(unidade2.ganharQuandoAtacadoPor(unidade1)) {
            System.out.println("Unidade vencedora " + unidade2.toString() + ".  Unidade perdedora " + unidade1.toString());
            unidade1.receberDano();
            if(unidade1.isVivo()) {
                System.out.println("Continua viva");
            } else {
                System.out.println("Morreu");
                tropas1.remove(indiceAleatorio1);
            }
        }
        else{
            System.out.println("Houve um Empate");
        }

    }

    if(tropas1.isEmpty()) {
        System.out.println("O jogador " + jogador1 + " ganhou, e o " + jogador2 + " perdeu");
    } else {
        System.out.println("O jogador " + jogador2 + " ganhou, e o " + jogador1 + " perdeu");
    }

    }
}
