package lab6;

public class Catapulta extends Unidade {

    public Catapulta() {
        setPontosVida(3);
    }

    @Override
    public boolean ganharQuandoAtacadoPor(Unidade u) {
        if( u instanceof Infantaria) {
            return true;
        }
        else if( u instanceof Cavalaria) {
            u.receberDano();
            return false;
        }
        return false;
    }

}
