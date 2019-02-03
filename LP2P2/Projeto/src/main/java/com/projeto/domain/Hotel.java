package com.projeto.domain;

import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.GenerationType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import java.util.List;
@Entity
public class Hotel {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer Id;
	private String name;
	
	  
    @OneToMany(cascade = CascadeType.ALL, mappedBy = "hotel")
	private List<Pessoa> pessoa;

	public Hotel() {
		
	}
	
	public Hotel(String name) {
		this.name = name;
	}
    

	 @OneToMany(cascade = CascadeType.ALL, mappedBy = "hotel")
	private List<Endereco> endereco;
	 
	 @OneToMany(cascade = CascadeType.ALL, mappedBy = "hotel")
	private List<Quarto> quartos;

	 
	public List<Quarto> getQuartos() {
		return quartos;
	}

	public List<Pessoa> getPessoa() {
		return pessoa;
	}


	public List<Endereco> getEndereco() {
		return endereco;
	}


	
	public void setName(String name){
		this.name= name;
	}
	
	public String getName() {
		return this.name;
	}

}
