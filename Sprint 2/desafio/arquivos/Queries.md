SELECT idCarro, classiCarro, marcaCarro , modeloCarro, anoCarro, idcombustivel, tipoCombustivel  
from tb_locacao tl 

SELECT *
from carros

INSERT INTO carros (idCarro, classiCarro, marcaCarro , modeloCarro, anoCarro, idcombustivel, tipocombustivel )
VALUES
    (98,'AKJHKN98JY76539','Fiat','Fiat Uno',2000,1,'Gasolina'),
	(99,'IKJHKN98JY76539','Fiat','Fiat Palio',2010,1,'Gasolina'),
	(3,'DKSHKNS8JS76S39','VW','Fusca 78',1978,1,'Gasolina'),
	(10,'LKIUNS8JS76S39','Fiat','Fiat 147',1996,1,'Gasolina'),
	(7,'SSIUNS8JS76S39','Fiat','Fiat 147',1996,1,'Gasolina'),
	(6,'SKIUNS8JS76S39','Nissan','Versa',2019,1,'Gasolina'),
	(2,'AKIUNS1JS76S39','Nissan','Versa',2019,2,'Etanol'),
	(4,'LLLUNS1JS76S39','Nissan','Versa',2020,2,'Etanol'),
	(1,'AAAKNS8JS76S39','Toyota','Corolla XEI',2023,3,'Flex'),
	(5,'MSLUNS1JS76S39','Nissan','Frontier',2022,4,'Diesel')
	
	
ALTER TABLE carros DROP COLUMN kmCarro;

CREATE TABLE locacoes (
    id_locacao INT PRIMARY KEY,
    id_cliente INT,
    idCarro INT,
    idVendedor INT,
    dataLocacao DATE,
    horaLocacao TIME,
    kmCarro INT,
    qtdDiaria INT,
    vlrDiaria DECIMAL(10, 2),
    dataEntrega DATE,
    horaEntrega TIME,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (idCarro) REFERENCES carros(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES vendedores(idVendedor)
);

CREATE TABLE carros (
    idCarro INT PRIMARY KEY,
    classiCarro VARCHAR(255),
    marcaCarro VARCHAR(255),
    modeloCarro VARCHAR(255),
    anoCarro INT,
    idcombustivel INT,
    tipocombustivel VARCHAR(255)
);

CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nomeCliente VARCHAR(255),
    cidadeCliente VARCHAR(255),
    estadoCliente VARCHAR(255),
    paisCliente VARCHAR(255)
);

CREATE TABLE vendedores (
    idVendedor INTEGER PRIMARY KEY,
    nomeVendedor VARCHAR(255),
    sexoVendedor SMALLINT,
    estadoVendedor VARCHAR(255)
);

INSERT INTO locacoes (id_locacao ,  id_cliente ,idCarro ,idVendedor, dataLocacao, horaLocacao,kmCarro, qtdDiaria, vlrDiaria,dataEntrega,horaEntrega  )
VALUES 
	(1,2,98,5,'2015-01-10','10:00',25412,2,100,'2015-01-12','10:00'),
	(2,2,98,5,'2015-02-10','12:00',29450,2,100,'2015-02-20', '12:00'),
	(3,3,99,6,'2015-02-13','12:00',20000,2,150,'2015-02-20','12:00'),
	(4,4,99,6,'2015-02-15','13:00',21000,5,150,'2015-02-20','13:00'),
	(5,4,99,7,'2015-03-02','14:00',21700,5,150,'2015-03-02','14:00'),
	(6,6,3,8,'2016-03-02','14:00',121700,10,250,'2016-03-02','14:00'),
	(7,6,3,8,'2016-08-02','14:00',131800,10,250,'2016-08-02','14:00'),
	(8,4,3,6,'2017-01-02','18:00',151800,10,250,'2017-01-02','18:00'),
	(9,4,3,6,'2018-01-02','18:00',152800,10,280,'2018-01-02','18:00'),
	(10,10,10,16,'2018-03-02','18:00',211800,10,50,'2018-03-02','18:00'),
	(11,20,7,16,'2018-04-01','11:00',212800,10,50,'2018-04-01','11:00'),
	(12,20,6,16,'2020-04-01','11:00',21800,10,150,'2020-04-01','11:00'),
	(13,22,2,30,'2022-05-01','08:00',10000,20,150,'2022-05-01','08:00'),
	(14,22,2,30,'2022-06-01','08:00',20000,20,150,'2022-06-01','08:00'),
	(15,22,2,30,'2022-07-01','08:00',30000,20,150,'2022-07-01','08:00'),
	(16,22,2,30,'2022-08-01','08:00',40000,20,150,'2022-08-01','08:00'),
	(17,23,4,31,'2022-09-01','08:00',55000,20,150,'2022-09-01','08:00'),
	(18,23,4,31,'2022-10-01','08:00',56000,20,150,'2022-10-01','08:00'),
	(19,23,4,31,'2022-11-01','08:00',58000,20,150,'2022-11-01','08:00'),
	(20,5,1,16,'2023-01-02','18:00',1800,10,880,'2023-01-02','18:00'),
	(21,5,1,16,'2023-01-15','18:00',8500,10,880,'2023-01-15','18:00'),
	(22,26,5,32,'2023-01-25','08:00',28000,5,600,'2023-01-25','08:00'),
	(23,26,5,32,'2023-01-31','08:00',38000,5,600,'2023-01-31','08:00'),
	(24,26,5,32,'2023-02-06','08:00',48000,5,600,'2023-02-06','08:00'),
	(25,26,5,32,'2023-02-12','08:00',68000,5,600,'2023-02-12','08:00'),
	(26,26,5,32,'2023-02-18','08:00',78000,1,600,'2023-02-18','08:00')

INSERT INTO vendedores (idVendedor,  nomeVendedor,sexoVendedor,estadoVendedor )
VALUES 
	(5,'Vendedor cinco', 0, 'São Paulo'),
	(6,'Vendedora seis', 1, 'São Paulo'),
	(7,'Vendedora sete', 1, 'Rio de Janeiro'),
	(8,'Vendedora oito', 1, 'Minas Gerais'),
	(16,'Vendedor dezesseis', 0, 'Amazonas'),
	(30,'Vendedor trinta', 0, 'Rio Grande do Sul'),
	(31,'Vendedor trinta e um', 0, 'Ceará'),
	(32,'Vendedora trinta e dois', 1, 'Mato Grosso do Sul')

INSERT INTO clientes (id_cliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
VALUES
    (2, 'Cliente dois', 'São Paulo', 'São Paulo', 'Brasil'),
    (3, 'Cliente tres', 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil'),
    (4, 'Cliente quatro', 'Rio de Janeiro', 'Rio de Janeiro', 'Brasil'),
    (6, 'Cliente seis', 'Belo Horizonte', 'Minas Gerais', 'Brasil'),
    (10, 'Cliente dez', 'Rio Branco', 'Acre', 'Brasil'),
    (20, 'Cliente vinte', 'Macapá', 'Amapá', 'Brasil'),
    (22, 'Cliente vinte e dois', 'Porto Alegre', 'Rio Grande do Sul', 'Brasil'),
    (23, 'Cliente vinte e tres', 'Eusébio', 'Ceará', 'Brasil'),
    (5, 'Cliente cinco', 'Manaus', 'Amazonas', 'Brasil'),
    (26, 'Cliente vinte e seis', 'Campo Grande', 'Mato Grosso do Sul', 'Brasil')