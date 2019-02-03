package com.listaheranca.questao2;

public class Empregado {
	private String nome;
	protected double salario;
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public double getSalario() {
		return salario;
	}
	public void setSalario(double salario) {
		this.salario = salario;
	}
	@Override
	public String toString() {
		return "Nome do Empregado=" + nome + ", salario" + salario;
	}
	
	
	
	}
