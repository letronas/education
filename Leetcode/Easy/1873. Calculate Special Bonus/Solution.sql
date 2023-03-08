SELECT
    employee_id
    ,CASE WHEN MOD(employee_id,2) = 1 AND lower(name) not like 'm%' 
	      THEN salary 
		  ELSE 0 
	END as bonus 
FROM Employees
ORDER BY employee_id