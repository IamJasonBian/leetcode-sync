# Id 2, sets the id as an array. 
# array with the ids

DELETE
FROM Person
WHERE Id NOT IN (SELECT a.Id
                FROM (SELECT min(id) Id
                        FROM Person
                        GROUP BY Email
                        ) a
                 );
