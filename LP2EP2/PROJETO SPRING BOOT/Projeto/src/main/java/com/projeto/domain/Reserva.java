package com.projeto.domain;
import java.util.List;
public class Reserva {
	private String date;
	private List<Reserva> reservas;

	public Reserva() {
	}

	public Reserva(String date) {
		this.date = date;
	}

	public String getDate() {
		return date;
	}

	public void setDate(String date) {
		this.date = date;
	}
	
	public List<Reserva> reservas(Reserva a){
		reservas.add(a);
		return reservas;
   	}
	
	

}
