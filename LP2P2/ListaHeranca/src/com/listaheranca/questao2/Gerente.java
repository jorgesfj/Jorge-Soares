package com.listaheranca.questao2;

public class Gerente extends Empregado {
	private String departamento;
	
	public Gerente(String departamento) {
		super();
		this.departamento = departamento;
	}

	public String getDepartamento() {
		return departamento;
	}

	public void setDepartamento(String departamento) {
		this.departamento = departamento;
	}

	@Override
	public String toString() {
		return "Departamento=" + departamento + "Nome = "+super.getNome()+" Salario =" + super.salario;
	}
	
	

}
