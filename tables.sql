drop table if exists Customer;

     create table Customer (
     	    id			int		primary key,
	    first_name 		varchar(64)	not null,
	    last_name		varchar(64)	not null,
	    phone 	  	int,
	    email	  	varchar(64)	     
     ) ENGINE=INNODB;

drop table if exists Customer_Transaction;

     create table Customer_Transaction (
     	    transaction_id		 int	primary key	references transaction(id),
     	    customer_id		 int	not null	references Customer(id)
     ) ENGINE=INNODB;

drop table if exists Transaction;

     create table Transaction (
     	    id			int		primary key,
	    amount		int,
	    price		double		not null,
	    on_credit		boolean		not null,
 	    data_transaction	date		not null	    
     ) ENGINE=INNODB;

-- add some info --

insert into Customer values (1, 'vasco', 'conde', '960008885', 'vasconde@gmail.com');

insert into Customer values (2, 'nuno', 'nunes', '919623469', 'nunnes00@gmail.com');

insert into Customer values (3, 'gilberto', 'conde', '96534234', 'vitamina.gil@gmail.com');

insert into Transaction values (1, 2, 23.00, false, '2010-03-12');

insert into Transaction values (2, 100, 3000.00, false, '2010-3-31');

insert into Transaction values (3, 32, 234.00, true, '2010-2-21');

insert into Customer_Transaction values (1,1);

insert into Customer_Transaction values (3,1);

insert into Customer_Transaction values (2,3);
