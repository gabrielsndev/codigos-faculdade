package lab6;
public class Infantaria extends Unidade {

    public Infantaria() {
        setPontosVida(1);
    }
    
    @Override
    public boolean ganharQuandoAtacadoPor(Unidade u) {
        if( u instanceof Catapulta) {
            u.receberDano();
            return false;
        }
        else if( u instanceof Cavalaria) {
            return true;
        }
        return false;
    }
}
