package com.projeto.resource;
import java.util.List;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;

import com.projeto.repository.HotelRepository;
import com.projeto.domain.Hotel;

@RestController
public class HotelResource{

	@Autowired
	private HotelRepository repository;
	
	@GetMapping("/hotel")
	public List<Hotel> getAllHotel(){
		List<Hotel> hoteis= repository.findAll();
		
		return hoteis;
	}
}