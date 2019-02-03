package com.projeto.resource;
import java.util.List;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;

import com.projeto.repository.PessoaRepository;
import com.projeto.domain.Pessoa;

@RestController
public class PessoaResource {

	@Autowired
	private PessoaRepository repository;
	
	@GetMapping("/pessoas")
	public List<Pessoa> getAllPessoa(){
		List<Pessoa> pessoas = repository.findAll();
		
		return pessoas;
	}
}