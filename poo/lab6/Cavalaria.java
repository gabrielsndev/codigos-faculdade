package lab6;
public class Cavalaria extends Unidade {

    public Cavalaria() {
        setPontosVida(2);
    }

    @Override
    public boolean ganharQuandoAtacadoPor(Unidade u) {
        if( u instanceof Infantaria) {
            u.receberDano();
            return false;
        }
        else if( u instanceof Catapulta) {
            return true;
        }
        return false;
    }
    
}