package com.listapolimorfismo.questao5;

public class TrabalhadorHora extends Empregado {
	private double hora;
	private double salarioHora;
	
	public double calcularGanho() {
		return this.salarioHora * this.hora;
	}
}
