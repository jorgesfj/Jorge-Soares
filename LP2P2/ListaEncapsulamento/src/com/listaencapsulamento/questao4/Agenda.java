package com.listaencapsulamento.questao4;
import java.util.List;



public class Agenda {
	
	private List<Nota> notas;
	
	
	public List<Nota> adicionar(Nota nota){
		notas.add(nota);
		return notas;
	}
	
	public List<Nota> remover(Nota nota){
		notas.remove(nota);
		return notas;
	}
	
	public void atualizar(Nota nota) {
		
	}
	
	public void listarTrue() {
		for(int i = 0; i<=notas.size();i++) {
			}
		}
	
	public void listarFalse() {
		
	}
	
	public void Finalizar() {
		
	}
	
	
}
