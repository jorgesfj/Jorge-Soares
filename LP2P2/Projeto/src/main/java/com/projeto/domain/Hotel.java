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
	 

//	}
//	public void setTelefone(Telefone telefone) {
//		this.telefone=telefone;
//	}
//	public void setEndereco(Endereco endereco) {
//		this.endereco = endereco;
//	}
//	public void setQuarto(Quarto quarto) {
//		this.quarto = quarto;
//	}

//	
//	public Telefone getTelefone() {
//		return this.telefone;
//	}
//	public Endereco getEndereco() {
//		return this.endereco;
//	}
//	public Quarto getQuarto() {
//		return this.quarto;
//	}
//	
	
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
