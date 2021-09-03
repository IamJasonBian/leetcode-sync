SELECT
        WNDW.DEPARTMENT, WNDW.EMPLOYEE, WNDW.SALARY 
      FROM
        (
            #Dense Rank to create full ranking
            
            SELECT
                EMPLOYEE,
                SALARY,
                DEPARTMENT,
                DENSE_RANK() OVER(PARTITION BY DEPARTMENT ORDER BY SALARY DESC) RNK
            FROM
            
                #Left join to form full database
            
                (SELECT B.Name as DEPARTMENT, A.Name as EMPLOYEE, A.Salary as SALARY
                    FROM 
                    Employee as A LEFT JOIN
                    Department as B on A.DepartmentId = B.Id ) EMPLOYEE
        ) WNDW
        
        #Filter for top 3
        WHERE WNDW.RNK < 4
