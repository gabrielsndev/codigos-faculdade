package lab6;


public abstract class Unidade {
    private int pontosVida;

    public int getPontosVida() {
        return pontosVida;
    }

    public void setPontosVida(int pontosVida) {
        this.pontosVida = pontosVida;
    }

    public void receberDano() {
        this.pontosVida--;
    }

    public boolean isVivo() {
        if(this.pontosVida == 0) {
            return false;
        }
        return true;
    }

    public abstract boolean ganharQuandoAtacadoPor(Unidade u);

}
