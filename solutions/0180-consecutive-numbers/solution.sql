# Write your MySQL query statement below
with cte as(
select num as n1, lead(num,1)over(order by id)as n2, lead(num,2)over(order by id)as n3
from logs)

select distinct n1 as ConsecutiveNums from cte 
where n1=n2 and n2=n3
