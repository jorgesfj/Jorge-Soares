package com.projeto.domain;

public class Funcionario extends Pessoa {
	private String sector;
	
	public Funcionario() {
		
	}
	
	public Funcionario(String sector) {
		super();
		this.sector = sector;
	}
	
	public void setSector(String sector) {
		this.sector = sector;
	}
	
	public String getSector() {
		return this.sector;
	}
}
