package com.projeto.domain;

public class Telefone {
	
	private String ddd;
	private String number;
	
	public Telefone() {
		
	}
	
	public Telefone(String ddd, String number) {
		this.ddd = ddd;
		this.number = number;
	}
	public void setDDD(String ddd) {
		this.ddd = ddd;
	}
	
	public void setNumber(String number) {
		this.number = number;
	}
	
	public String getDDD() {
		return this.ddd;
	}
	
	public String getNumber() {
		return this.number;
	}

}
