### Northwind Database sample 

## Use Select Statement to select columns

#### Select everything from an existing table 
```
select * from Shippers
```

#### Count how many rows are in a specefic table
```
select count(*) from Shippers
```

#### Creating an alias(new column)
```
select count(*) as numberofRows from Shippers
```

#### Selecting specefic columne from Database
```
select CateogoryName, Description
from Categories
```

## Use the WHERE clause to apply conditions

#### Example 1
```
select FirstName, LastName, HireDate, Title, Country
from Employees
WHERE Title = 'Sales Representative' AND Country = 'USA'
```

#### Example 2 - using a NOT
```
select SupplierId, ContactName, ContactTitle
from Suppliers
WHERE ContactTitle != 'Marketting Manager'
```

#### Example 2 - using a IN
```
select OrderID
from Orders
WHERE ShipCountry IN ('France', 'Belgium')
```

## Applying GROUP BY to group data by columns

#### Example 1 - Select Disctinct
```
select Country
from Customers
GROUP BY Country
```

#### Example 2 - Count the number of customer per country
```
select Country, count(CustomerId) as NumberOfCustomers
from Customers
GROUP BY Country
```

#### Example 3 - Count the number of customer per country in descending order
```
select Country,City, count(CustomerId) as NumberOfCustomers
from Customers
GROUP BY Country, City
ORDER BY NumberOfCustomers DESC
```


### Quiz
###### Your Task:

###### Retrieve all orders made by a specific customer whose CustomerID is ‘ALFKI’.
```
Select *
From Orders
Where CustomerID = 'ALFKI'
```
###### Retrieve all orders made in a specific year 1997. (Use the SQL function YEAR() to access the year of OrderDate).
```
Select *
From Orders
Where Year(OrderDate) = 1997
```
###### Retrieve the total number of orders for each customer.
```
Select CustomerID, Count(OrderId)
From Orders
Group By CustomerID
```
###### Retrieve the ProductID, Sum of Orders by ProductID and the TotalOrderAmount as the SUM of UnitPrice and Quantity.
```
Select ProductId, Count(OrderId) as CountOrder,
Sum(UnitPrice * Quantity) as TotalOrderAmount
From [OrderDetails]
Group By ProductID
```


