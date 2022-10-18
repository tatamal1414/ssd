create table subjects (
    id serial PRIMARY KEY NOT NULL,
    subject varchar(20) NOT NULL,
    department_id int NOT NULL,
    major_id int NOT NULL,
    FOREIGN KEY(department_id) 
    REFERENCES departments(id),

    FOREIGN KEY(major_id)
    REFERENCES majors(id)
);