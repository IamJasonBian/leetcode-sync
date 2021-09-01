CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT
        WNDW.SALARY
      FROM
        (
            SELECT
                SALARY,
                DENSE_RANK() OVER(ORDER BY SALARY DESC) RNK
            FROM
                EMPLOYEE
        ) WNDW
      WHERE
        WNDW.RNK = N
      LIMIT 1
  );
END
