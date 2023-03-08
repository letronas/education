SELECT 
    COALESCE(EMP.employee_id, SAL.employee_id) employee_id 
FROM Employees EMP
FULL JOIN Salaries SAL 
       ON EMP.employee_id = SAL.employee_id
WHERE EMP.employee_id IS NULL OR SAL.employee_id IS NULL
ORDER BY COALESCE(EMP.employee_id, SAL.employee_id)