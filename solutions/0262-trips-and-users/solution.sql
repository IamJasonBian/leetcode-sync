# Write your MySQL query statement below
#The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

select A.Request_at as 'Day', ROUND(COUNT(CASE WHEN Status = 'cancelled_by_driver' or Status = 'cancelled_by_client' THEN 1 END)/COUNT(*), 2) as 'Cancellation Rate'

from
    (Select Request_at, Status, CASE When (B.Banned = "Yes") or (C.Banned = "Yes") then 1 else 0 END as "total_unbanned"

    from Trips as A
        left join Users as B on A.Client_Id = B.Users_Id
        left join Users as C on A.Driver_Id = C.Users_Id

    where CASE When (B.Banned = "Yes") or (C.Banned = "Yes") then 1 else 0 END = 0
    and Request_at between "2013-10-01" and "2013-10-03") as A
group by Day
