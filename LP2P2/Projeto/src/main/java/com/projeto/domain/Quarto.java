package com.projeto.domain;

import javax.persistence.Entity;

import javax.persistence.CascadeType;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;
import java.util.List;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.GenerationType;

@Entity
public class Quarto{
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Integer id;
	private String type;
	private boolean isBusy;
	private int roomNumber;
	 
	@ManyToOne(optional = false)
	@JoinColumn(name = "hotel_id")
	private Hotel hotel;

	
	@OneToMany(cascade = CascadeType.ALL, mappedBy = "quarto")
	private List<Cama> cama;
	
	
	public Quarto() {
	}
	public Quarto(String type, boolean isBusy, int roomNumber) {
		this.type = type;
		this.isBusy = isBusy;
		this.roomNumber = roomNumber;
	}
	public String getType() {
		return type;
	}
	public void setType(String type) {
		this.type = type;
	}
	public boolean isBusy() {
		return isBusy;
	}
	public void setBusy(boolean isBusy) {
		this.isBusy = isBusy;
	}
	public int getRoomNumber() {
		return roomNumber;
	}
	public void setRoomNumber(int roomNumber) {
		this.roomNumber = roomNumber;
	}

	public List<Cama> getCama() {
		return cama;
	}
	public void setCama(List<Cama> cama) {
		this.cama = cama;
	}
	public String checkAvailability() {
		if(isBusy) {
			return "OCUPADO";
		}else {
			return "LIVRE";
		}
	}
	
}
