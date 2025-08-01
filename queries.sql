create table estudiante(Identificacion int primary key ,
Nombre varchar(50), Codigo varchar(50), Correo varchar(50),
Edad int);

show tables;

desc estudiante;

insert into estudiante(Identificacion,Nombre,Codigo,Correo,Edad) 
values(10,"Edwin","EB2025","edwinfincom@gmail.com",24);

select * from estudiante;

select identificacion, Nombre from estudiante;

insert into estudiante(Identificacion,Nombre,Codigo,Correo,Edad) 
values(11,"Laura","LC2025","laurachp2201@gmail.com",24);
insert into estudiante(Identificacion,Nombre,Codigo,Correo,Edad) 
values(12,"Mateo","MR2025","mateo@gmail.com",34);
insert into estudiante(Identificacion,Nombre,Codigo,Correo,Edad) 
values(13,"Sofia","SL2025","sofia@gmail.com",22);

select * from estudiante;

select * from estudiante order by Nombre;

select Identificacion,Nombre,Edad from estudiante order by Edad;

select max(Edad) from estudiante;
select min(Edad) from estudiante;

select * from estudiante where Edad =
(select max(Edad) from estudiante);

create table curso(CodigoCurso int primary key, Curso varchar(50), 
Docente varchar(50), Horario varchar(50));

insert into curso(CodigoCurso,Curso,Docente,Horario) 
values("1","Programación","Jorge","Martes&Jueves: 5pm-9pm, Sabados 11am-5pm"),
("2","Analisis de Datos","Luisa","Martes&Jueves: 5pm-9pm, Sabados 7am-12pm"),
("3","Block Chain","Alejandro","Martes&Jueves: 12am-5pm, Sabados 7am-11am");

select * from curso;

alter table estudiante add column CursoEstudiante int;
alter table estudiante add foreign key (CursoEstudiante)
references curso(CodigoCurso);

update estudiante set CursoEstudiante = 1 where Identificacion =10;
update estudiante set CursoEstudiante = 2 where Identificacion =11;
update estudiante set CursoEstudiante = 3 where Identificacion =12;
update estudiante set CursoEstudiante = 3 where Identificacion =13;

select * from estudiante;

select * from curso inner join estudiante on 
estudiante.CursoEstudiante = curso.CodigoCurso;

select curso.Curso,estudiante.Nombre
from curso inner join estudiante on
estudiante.CursoEstudiante = curso.CodigoCurso;

select avg(Edad) from estudiante;

select * from estudiante where edad > 
(select avg(Edad) from estudiante);