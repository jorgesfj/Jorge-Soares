package com.projeto.repository;


import org.springframework.data.jpa.repository.JpaRepository;

import com.projeto.domain.Quarto;
public interface QuartoRepository extends JpaRepository<Quarto, Integer> {

}
