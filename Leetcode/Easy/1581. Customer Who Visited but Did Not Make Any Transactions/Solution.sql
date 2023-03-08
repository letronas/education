SELECT
 Vs.customer_id
 ,COUNT (*) as count_no_trans 
FROM Visits Vs
LEFT JOIN Transactions Tr
       ON Vs.visit_id = Tr.visit_id
WHERE Tr.amount is null
GROUP BY Vs.customer_id