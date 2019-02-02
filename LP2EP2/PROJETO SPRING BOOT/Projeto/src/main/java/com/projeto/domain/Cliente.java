package com.projeto.domain;

import java.util.List;


public class Cliente extends Pessoa {
	private int amountOfOccupations;
	
	
	public Cliente() {
	}
	public Cliente(int amountOfOccupations) {
		this.amountOfOccupations = amountOfOccupations;
	}

	
public int getAmountOfOccupations() {
		return amountOfOccupations;
	}
	public void setAmountOfOccupations(int amountOfOccupations) {
		this.amountOfOccupations = amountOfOccupations;
	}
	
	public List<Reserva> calculateOccupations(List<Reserva> reservas){
		return reservas;
	}
	
	@Override
	public String toString() {
		return "Cliente [amountOfOccupations=" + amountOfOccupations + "]";
	}
	
	
}
