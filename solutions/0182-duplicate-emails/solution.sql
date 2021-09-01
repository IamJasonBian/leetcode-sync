# Write your MySQL query statement below

Select A.Email as Email from
    (Select Email, count(*) as email_count 
    from Person
    group by Email) as A
where email_count > 1
