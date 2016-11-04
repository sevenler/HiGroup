
create table user
(
    id int not null,
    email varchar(100) not null,
    password varchar(100),
    name varchar(100),
    description varchar(100),
    PRIMARY KEY (id)
)
