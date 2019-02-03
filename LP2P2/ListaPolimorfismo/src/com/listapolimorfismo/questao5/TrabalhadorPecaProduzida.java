package com.listapolimorfismo.questao5;

public class TrabalhadorPecaProduzida extends Empregado{
	private int numeroDeItens;
	private int remuneracao;
	
	public double calcularGanho() {
		return this.remuneracao * this.numeroDeItens;
	}

}
