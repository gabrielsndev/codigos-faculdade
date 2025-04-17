// Crie também uma classe chamada Nutricionista, que será responsável por realizar a avaliação física do Paciente através do cálculo do IMC.
// O IMC é calculado dividindo o peso do paciente pela altura elevada ao quadrado (IMC = peso / altura²).
// A classe Nutricionista deve conter um método chamado avaliarIMC, que receberá um objeto do tipo Paciente e retornará uma String
// correspondente à classificação do IMC do paciente.

package lista3;

public class Nutricionista {
 

    public ResultadoImc calcularImc(Paciente paciente) {
        double imc = paciente.getPeso() / Math.pow(paciente.getAltura(), 2);
        ResultadoImc status = ResultadoImc.OBESIDADE;
       if (imc < 18.5) {
            status = ResultadoImc.BAIXOPESO;
       } else if (imc >= 18.5 & imc <= 24.99) {
            status = ResultadoImc.NORMAL;
       } else if (imc >= 25.0 & imc <= 29.99) {
            status = ResultadoImc.SOBREPESO;
        }
        return status;
    }
    
}