package com.listaencapsulamento.questao3;

public class Conta {
	private int numero;
	private double saldo;
	
	public boolean deposito(int numero) {
		if(this.numero == numero) {
			return true;
		}else {
			return false;
		}
	}
	
	public boolean saque(int numero, double valor) {
		if(this.numero == numero) {
			if(this.saldo <= valor) {
				return true;
			}else {
				return false;
			}
		}else {
			return false;
		}
	}
	
	
	
	
	

}
