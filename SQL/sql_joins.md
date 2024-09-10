
## SQL JOIN

#### Develop an understanding of inner, left and right joins
###### Project Structure
```
Use Bookstore;
```
Task 1: you will be able to develop an inner join.
```
Select orderinfo.itemid, customer.customername
FROM orderinfo
INNER JOIN customer ON orderinfo.customerid = customer.customerid;
```

Refactor:
```
Select o.itemid, c.customername
FROM orderinfo AS o
INNER JOIN customer AS c ON o.customerid = c.customerid;
```

Quiz:
Item table and aurthor table
Retrieve title of the book an aurthor name

```
Select i.booktitle, a.authorname
FROM item AS i
INNER JOIN author AS a ON a.authorid = i.authorid;
```

Task 2: you will be able to develop a left join.
```
Select i.booktitle, a.authorname
FROM item AS i
LEFT JOIN author AS a ON a.authorid = i.authorid
ORDER BY i.booktitle;
```

Quiz:
All of cuctomer Customer table on left
Order item from order table

```
Select c.customername, o.itemid
FROM customer AS c
LEFT JOIN orderinfo AS o ON c.customerid=o.customerid
ORDER BY c.customername;

```
Task 3: you will be able to develop a right join.
```
SELECT o.itemid, c.customername
FROM orderinfo AS o
RIGHT JOIN customer AS c on o.customerid=c.customerid
ORDER BY c.customer
```

Quiz
- Right join on the item table, bring back author name from autors table

```
Select a.authorname, i.booktitle
From author AS a
RIGHT JOIN item AS i ON a.authorid=i.authorid
ORDER BY a.authorname
```

#### Develop an understanding of the self-join and cross-join

Task 4: you will be able to create a self join and cross join.
Self-join: When a table join it self

```
SELECT e.firstname AS EmployeeName, em.firstname AS ManagerName
FROM employees e
INNER JOIN employees em
ON e.managerid=em.managerid
```

Cross Join: Result set, rows X rows (all results returned)
```
SELECT *
FROM item
CROSS JOIN author
```

#### Develop an understanding of the UNION and UNION ALL keywords.
Task 5: you will be able to utilise the union and union all.

Union- Unique values
```
SELECT city FROM customer
UNION
SELECT city FROM supplier
ORDER BY city
```

Union all- all result within result sets, even duplicates
```
SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers
ORDER BY City;
```
