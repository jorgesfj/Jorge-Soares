package com.listaheranca.questao2;

public class Vendedor extends Empregado{
	private double percentualComissao;

	public Vendedor(double percentualComissao) {
		super();
		this.percentualComissao = percentualComissao;
	}
	
	public double calcularSalario() {
		double total = super.salario + this.percentualComissao;
		return total;
		
	}

	public double getPercentualComissao() {
		return percentualComissao;
	}

	public void setPercentualComissao(double percentualComissao) {
		this.percentualComissao = percentualComissao;
	}

	@Override
	public String toString() {
		return "Nome do Empregado=" + getNome() + ", salario" + salario + "percentualComissao=" + percentualComissao + ", Salario com comissao" +calcularSalario();
	}
	
	

}
