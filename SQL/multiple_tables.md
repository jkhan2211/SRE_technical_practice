The hands on project on Multiple-Table SQL Queries is divided into following tasks:

##### Task 1: Joining Two Tables with WHERE   
```
SELECT deptname, emplastname,
empfirstname
FROM employee, department
WHERE deptid = empdeptid
ORDER BY deptname
``` 
##### Task 2: Understanding Table Relationships - 2 tables
```
SELECT bldname, deptname
FROM building, department
WHERE deptbuilding = bldid
ORDER BY bldname
```
##### Task 3: Joining Three or More Tables
Display a list of employee name in each department, and put them in the order by last name,
within department, within building name

Example 1:
```
SELECT bldname, deptname, emplastname, empfirstname
FROM building, department, employee
WHERE deptbuilding = bldid
AND empDeptID = DeptID
ORDER BY bldname, deptname, emplastname

```

Example 2:
```
SELECT projdesc, emplastname, empfirstname,
    Deptname, bldname
FROM building, department, employee, project
WHERE deptbuilding = bldid
AND empDeptID = DeptID
AND projmanager = empid
ORDER BY projdesc

```

##### Task 4: Adding Selection to the WHERE Clause
```
SELECT projdesc, empfirstname,
    empext, projbudget
FROM employee, project
WHERE empid = projmanager
AND projbudget > 100000
```

Quiz:
```
SELECT deptname, empfirstname, emplastname,
    emphiredate, empsalary
FROM department, employee
WHERE empdeptid = deptid
AND empsalary < 90000
ORDER BY deptname, empsalary
```
##### Task 5: The INNER JOIN  
```
SELECT bldname, deptname, empfirstname, emplastname, emphiredate, empsalary
FROM building
INNER JOIN department
INNER JOIN employee
ON deptBuilding = bldid
AND empdeptid = deptid
ORDER BY deptname. lastname
```
##### Task 6: The LEFT JOIN  
```
SELECT projdesc, emplastname
FROM project
LEFT JOIN
employee
ON empid = projmanager
ORDER BY projdesc
```