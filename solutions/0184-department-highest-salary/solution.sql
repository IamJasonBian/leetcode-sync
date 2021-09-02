
Select d1.Name as Department, e1.Name as Employee, e1.Salary as Salary
from Department d1
inner join Employee e1 on d1.Id = e1.DepartmentId
where e1.Salary in
(
    select max(e2.Salary)
    from Employee e2
    where e2.DepartmentId = d1.Id
)
