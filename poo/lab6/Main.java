package lab6;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Random rand = new Random();
        Scanner input = new Scanner(System.in);
        String jogador1 = input.nextLine();
        String jogador2 = input.nextLine();
        int carteira1 = 1200;
        int carteira2 = 1200;
        ArrayList<Unidade> tropas1 = new ArrayList<>();
        ArrayList<Unidade> tropas2 = new ArrayList<>();

        System.out.println("Escolha as tropas");
        System.out.println("Catapulta - 200");
        System.out.println("Cavalaria - 100");
        System.out.println("Infantaria - 50");


        while(carteira1 < 50) {
            String escolha = input.nextLine();
            switch (escolha) {
                case "infantaria":
                    if(carteira1 >= 50) {
                        Infantaria infantaria = new Infantaria();
                        tropas1.add(infantaria);
                    } else {
                        System.out.println("Impossível comprar essa tropa");
                    }
                    break;
                    
                case "Cavalaria":
                    if( carteira1 >= 100) {
                        Cavalaria cavalaria = new Cavalaria();
                        tropas1.add(cavalaria);
                    } else {
                        System.out.println("Impossível comprar essa tropa");
                    }
                    break;
                
                case "Catapulta":
                    if( carteira1 >= 200) {
                        Catapulta catapulta = new Catapulta();
                        tropas1.add(catapulta);
                    } else {
                        System.out.println("Impossível comprar essa tropa");
                    }
                    break;

                default:
                    System.out.println("Tropa inválida");
                    break;
            }
        }


        while(carteira2 < 50) {
            String escolha = input.nextLine();
            switch (escolha) {
                case "infantaria":
                    if(carteira2 >= 50) {
                        Infantaria infantaria = new Infantaria();
                        tropas2.add(infantaria);
                    } else {
                        System.out.println("Impossível comprar essa tropa");
                    }
                    break;
                    
                case "Cavalaria":
                    if( carteira2 >= 100) {
                        Cavalaria cavalaria = new Cavalaria();
                        tropas2.add(cavalaria);
                    } else {
                        System.out.println("Impossível comprar essa tropa");
                    }
                    break;
                
                case "Catapulta":
                    if( carteira2 >= 200) {
                        Catapulta catapulta = new Catapulta();
                        tropas2.add(catapulta);
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

    while(!tropas1.isEmpty() || !tropas2.isEmpty()) {
        int indiceAleatorio1 = rand.nextInt(tropas1.size());
        int indiceAleatorio2 = rand.nextInt(tropas2.size());

        Unidade unidade1 = tropas1.get(indiceAleatorio1);
        Unidade unidade2 = tropas2.get(indiceAleatorio2);

        System.out.println("Unidades a batalhar: " + unidade1.toString() + " " + unidade2.toString());

        if(unidade1.ganharQuandoAtacadoPor(unidade2)) {
            System.out.println("Unidade vencedora" + unidade1.toString() + ".  Unidade perdedora" + unidade2.toString());
            if(unidade2.isVivo()) {
                System.out.println("Continua viva");
            } else {
                System.out.println("Morreu");
                tropas2.remove(indiceAleatorio2);
            }
        }
        else if(unidade2.ganharQuandoAtacadoPor(unidade1)) {
            System.out.println("Unidade vencedora" + unidade2.toString() + ".  Unidade perdedora" + unidade1.toString());
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
        System.out.println("O jogador " + jogador1 + "ganhou, e o " + jogador2 + "perdeu");
    } else {
        System.out.println("O jogador " + jogador2 + "ganhou, e o " + jogador1 + "perdeu");
    }

    }
}
