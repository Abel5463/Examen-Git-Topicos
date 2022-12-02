create database peliculas;

create table director(
id int not null primary key auto_increment,
nombre varchar(30) not null,
telefono int
);

create table genero(
    id int not null primary key auto_increment,
    nombreg varchar(30)
);

create table pelicula(
id int not null primary key auto_increment,
nombre_pelicula varchar(30) not null,
duracion int not null,
id_genero int not null,
id_director int not null,
constraint fkgenero foreign key (id_genero) REFERENCES genero(id) on update cascade  on delete cascade,
constraint fkdirector foreign key (id_director) REFERENCES director(id) on update cascade on delete cascade
);

INSERT INTO genero (nombreg) VALUES ('terror');
INSERT INTO genero (nombreg) VALUES ('comedia');
INSERT INTO genero (nombreg) VALUES ('drama');
INSERT INTO genero (nombreg) VALUES ('accion');

insert into director(nombre, telefono) values ('Gillermo del toro', 4136204);
insert into director(nombre, telefono) values ('Hector Ramos', 4208173);
insert into director(nombre, telefono) values ('James cabellun', 4115197);
insert into director(nombre, telefono) values ('Stiv Spilver', 911911);

insert into PELICULA (nombre_pelicula, duracion, id_genero, id_director) values ('Chavo del 8 3D',120,1,2);
insert into PELICULA (nombre_pelicula, duracion, id_genero, id_director) values ('Metaverso del mark',110,2,3);
insert into PELICULA (nombre_pelicula, duracion, id_genero, id_director) values ('Elmer el bailador',140,2,3);
insert into PELICULA (nombre_pelicula, duracion, id_genero, id_director) values ('El tec embrujado',120,1,4);
insert into PELICULA (nombre_pelicula, duracion, id_genero, id_director) values ('2 sem para salvar el semestre',110,4,3);
