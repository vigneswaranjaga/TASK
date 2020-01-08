CREATE DATABASE `employedb`; 
USE employedb;

create table tbl_user(
user_id integer PRIMARY KEY ,
user_full_name varchar(40)
);

insert into tbl_user(user_id, user_full_name) 
values (1, "Vigneswaran R J "),(2, "Merwin Rommel "),(3,"punnya Teresa"),(4,"Priya M"), (5,"jay R"), (6,"Brijith J"), (7, "John J");
select * from tbl_user;

create table tbl_role(
role_id integer PRIMARY KEY , 
role_name varchar(40)
);
insert into tbl_role(role_id, role_name) 
values (1001, "Manager "),
(1002, "Software Developer "),
(1003,"Team Lead"),
(1004,"IT");


select * from tbl_role;

create table tbl_user_role(
user_id integer  ,
role_id integer ,
CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES tbl_user(user_id) ,
CONSTRAINT fk_role FOREIGN KEY (role_id)  REFERENCES tbl_role(role_id)
);

insert into tbl_user_role(user_id,role_id) values (1, 1001 ),(2,1002),(2,1003),(3,1004),(4,1004),(5,1010),(6,1015);
select * from tbl_user_role;

select u.user_full_name , r.role_name from tbl_user as u 
join tbl_user_role as ur 
on u.user_id=ur.user_id
join tbl_role as r 
on r.role_id=ur.role_id
where r.role_name='IT';

SELECT * from tbl_user  where user_id not in (select user_id from tbl_user_role);

select user_id from tbl_user_role group by user_id having  count(user_id)>1;