package lab7;

public class Main {
    public static void main(String[] args) {
        Bartender garcom = new Bartender();
        Bebida b1;
        Bebida b2;
        double precoTotal = 0;
        
        try{
            b1 = garcom.prepararBebida();
            precoTotal = b1.getPreco();
        } catch(Exception e) {
            precoTotal = 0;
        }
        
        try{
            b2 = garcom.prepararBebida();
            precoTotal += b2.getPreco();
        } catch(Exception e) {
            precoTotal += 0;
        }
        
        System.out.println("O valor total das bebidas é: " + precoTotal);
        
        
    }
}
