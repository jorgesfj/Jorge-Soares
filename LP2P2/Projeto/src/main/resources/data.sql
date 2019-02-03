insert into hotel(id,name) values (000, 'NULO')
insert into pessoa(id,name,hotel_id) values (000,'NULO',000)

insert into hotel(id,name) values (1, 'Desenlace')
insert into pessoa(id,name,number,hotel_id) values (1,'Jorge','23423',1)
insert into endereco(id, number, city, pessoa_id,hotel_id) values (1,'234','A',1,000)
insert into endereco(id,number,city,pessoa_id,hotel_id) values (2,'677','H',000,1)

insert into quarto(id, is_Busy,ROOM_NUMBER, hotel_id) values (1,1,674,1)
insert into cama(id,tipo,quarto_id) values(1,'A',1)

