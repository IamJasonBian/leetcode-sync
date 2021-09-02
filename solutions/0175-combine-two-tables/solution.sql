# Write your MySQL query statement below
Select A.FirstName, A.LastName, B.City, B.State
from Person A
left join Address B on A.PersonId = B.PersonId 
