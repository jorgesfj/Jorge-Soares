package com.projeto.domain;

import java.util.List;


import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.OneToMany;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.GeneratedValue;


@Entity
public class Pessoa {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer id;
	private String name;
	private String number;
	
	@ManyToOne(optional = false)
	@JoinColumn(name = "hotel_id")
	private Hotel hotel;
	
	@OneToMany(cascade = CascadeType.ALL, mappedBy = "pessoa")
	private List<Endereco> enderecos;
	
	public Pessoa() {
		
	}

	public Pessoa(String name, String number) {
		this.name = name;
		this.number = number;
	}

	public void setName(String name) {
		this.name = name;
	}
	
	public void setNumber(String number) {
		this.number = number;
	}
	
	public String getName() {
		return this.name;
	}
	
	public String getNumber() {
		return this.number;
	}

	public List<Endereco> getEnderecos() {
		return enderecos;
	}

	public void setEnderecos(List<Endereco> enderecos) {
		this.enderecos = enderecos;
	}
	
}

