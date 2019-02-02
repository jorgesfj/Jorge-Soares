package com.projeto.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.projeto.domain.Hotel;

public interface HotelRepository extends JpaRepository<Hotel, Integer> {

}
