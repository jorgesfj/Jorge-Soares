package com.listaheranca.questao1;

public class IngressoVip extends Ingresso{
	private double valorAdicional;



	public double getValorAdicional() {
		return valorAdicional;
	}

	public void setValorAdicional(double valorAdicional) {
		this.valorAdicional = valorAdicional;
	}
	@Override
	public String toString() {
		return "Valor Adicional=" + valorAdicional;
	}
}
