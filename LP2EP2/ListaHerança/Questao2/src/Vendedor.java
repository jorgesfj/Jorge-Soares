public class Vendedor extends Empregado {
	private double percentualComissao;
	
	public double getPercentualComissao() {
		return percentualComissao;
		}
	
	public void setPercentualComissao(double percentualComissao) {
		this.percentualComissao = percentualComissao;
		}
		

	public Vendedor(String nome, float salario, double percentualComissao) {
		super(nome, salario);
		this.percentualComissao = percentualComissao;	
	}
	double total = super.salario + (super.salario*this.percentualComissao);
	
	public double calcularSalario(float salario, float percentualComissao) {
		return total;
	}
	
	public String toString(String nome, float salario, double pecentualComissao) {
			return "O funcionário: " +super.getNome()+" Tem salario de : " +super.salario+ "E salario com comissao de: " + total ;
	}
}
