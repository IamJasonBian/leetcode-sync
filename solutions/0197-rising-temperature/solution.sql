# Write your MySQL query statement below

select 
    weather.id as 'Id'
from 
    weather 
        join
    weather w on datediff(weather.recordDate, w.recordDate) = 1
        And weather.Temperature > w.Temperature
