package com.listaheranca.questao1;

public class Main {
	public static void main(String[] args) {
		
		Ingresso I1 = new Ingresso();
		IngressoVip Iv = new IngressoVip();
		
		I1.setValor(3.5);
		Iv.setValorAdicional(2.6);
		
		System.out.println(I1.getValor());
		System.out.println(Iv.getValorAdicional());
	}
}
