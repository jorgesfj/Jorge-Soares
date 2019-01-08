
public class TrabalhadorHora extends Empregado {
	private double salarioHora;
	private int qtdHoras;
	
	public double getSalarioHora() {
		return salarioHora;
	}
	public void setSalarioHora(double salarioHora) {
		this.salarioHora = salarioHora;
	}
	public int getQtdHoras() {
		return qtdHoras;
	}
	public void setQtdHoras(int qtdHoras) {
		this.qtdHoras = qtdHoras;
	}
	public double calcularGanho() {
		return 0;
	}
}
