## Manipulating Data with SQL
The hands on project on Manipulating Data with SQL is divided into following tasks:

##### Task 1: Know Your Tables    
##### Task 2: The INSERT Command
```
insert into Product
values
(377, 'Outdoor-2-Gallon-CoolerPack','ny-10',20.20,'2020-05-10')
```
##### Task 3: When it Doesn't Work

##### Task 4: The UPDATE Command
```
update Product
set prodcost = (prodcost*1.07)
```
##### Task 5: The Batch Load  
```
create table Customer
(CustId integer primary key,
CustLastName char(20),
CustFirstName char(15),
CustDiscount decimal(5,2)
);
```

##### Task 5.5: The Batch Load  
```
insert into Customer
values
(220000, 'Jonas', 'Ricky', 0),
(330000, 'Chow', 'Gagner', 5)

```

##### Task 6: DELETE and DROP  

```
delete from Customer
where CustID = 220000
```

```
delete from Customer
where CustDiscoutn = 5
```
