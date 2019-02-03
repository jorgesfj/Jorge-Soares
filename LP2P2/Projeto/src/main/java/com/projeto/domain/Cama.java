package com.projeto.domain;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.GenerationType;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;

@Entity
public class Cama {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer id;
	private String tipo;
	
	@ManyToOne(optional = false)
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
