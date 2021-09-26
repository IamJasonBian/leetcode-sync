with CTE as

(
Select dp.Name as Department, e1.Name as Employee, e1.Salary as Salary, 
    DENSE_RANK() OVER (Partition by e1.DepartmentId Order by e1.Salary desc) as rk
from Employee as e1
Inner join department dp
on e1.DepartmentId = dp.Id
    )
    
select Department, Employee, Salary from CTE 

where rk <= 3
order by Department

