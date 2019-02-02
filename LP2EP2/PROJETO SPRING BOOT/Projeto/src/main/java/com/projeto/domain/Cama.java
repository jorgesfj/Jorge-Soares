package com.projeto.domain;

import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;

public class Cama {
	
	private String tipo;
	
	@ManyToOne(optional = true)
	@JoinColumn(name = "quarto_id")
	private Quarto quarto;
	
	public Cama() {
		 
	}
	
	public Cama(String tipo) {
		this.tipo = tipo;
	}
	
	
	public void setTipo(String tipo) {
		this.tipo = tipo;
	}
	public String getTipo() {
		return this.tipo;
	}
	
	
}
