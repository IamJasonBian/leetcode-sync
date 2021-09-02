# Write your MySQL query statement below
Select A.Name as 'Customers'
from Customers as A
left outer join Orders as B
on A.Id = B.CustomerID
where B.CustomerId IS NULL
