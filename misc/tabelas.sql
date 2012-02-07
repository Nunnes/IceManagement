CREATE TABLE customer
(
C_Id                    int,
LastName       varchar(255),
FirstName      varchar(255),
Phone                int,
Email                  varchar(255),
PRIMARY KEY (C_Id)
);

INSERT INTO customer
VALUES (1, 'Conde', 'Vasco', 960008885, 'vasconde@gmail.com');

INSERT INTO customer
VALUES (2, 'Nunes', 'Nuno', 919623469, 'nunnes00@gmail.com');