package com.listapolimorfismo.questao5;

public class TrabalhadorComissionado extends Empregado{
	private double salario;
	private double comissao;
	
	public double calcularGanho() {
		return this.salario + this.comissao;
	}

}
