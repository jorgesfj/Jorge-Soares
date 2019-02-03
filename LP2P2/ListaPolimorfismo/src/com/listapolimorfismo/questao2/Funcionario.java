package com.listapolimorfismo.questao2;

public class Funcionario {
	
	private String nome;
	private String cpf;
	private String email;
	private int registroUnico;
	private String dataNascimento;
	private String funcao;
	private String senha;
	
	
	public boolean realizarLogin(String email, String senha) {
		if((this.email == email)&&(this.senha == senha)) {
			System.out.println(this.nome +"é"+this.funcao);
			return true;
		}else {
			return false;
		}
	}
	
	public boolean realizarLogin(int registroUnico, String senha) {
		if((this.registroUnico == registroUnico)&&(this.senha == senha)) {
			System.out.println(this.nome +"é"+this.funcao);
			return true;  
		}else {
			return false;
		}
	
	}
}