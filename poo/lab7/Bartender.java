package lab7;
import java.util.Scanner;

public class Bartender{
    
    public Bebida prepararBebida() throws Exception{
        Bebida b = null;
        Scanner input = new Scanner(System.in);
        System.out.println("1 para Pitu e 2 para Uísque");
        System.out.println("Digite que bebida deseja: ");
        String opcao = input.nextLine();
        switch(opcao){
            case "1":
                b = new Pitu();
                break;
                
            case "2":
                b = new Uisque();
                break;
        }
        boolean parar = true;
        while(parar) {
            System.out.println("Menu de complementos: ");
            System.out.println("Digite 1 para adicionar um Limão");
            System.out.println("Digite 2 para adicionar Sal");
            System.out.println("Digite 3 para não adicionar mais complementos");
                    
            opcao = input.nextLine();
            
            switch(opcao){
                case "1":
                    b = new Limao(b);
                    break;
                case "2":
                    b = new Sal(b);
                    break;
                case "3":
                    parar = false;
                    break;
            }
                    
            if (b.getTeor() > 1.2f) {
                throw new AlcoolDemaisException();
            }
            if (b.getTeor() < 0f) {
                throw new TeorAlcoolicoNegativoException();
            }
        }
        
        return b;
        
    }
}