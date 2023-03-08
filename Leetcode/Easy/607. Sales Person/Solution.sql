SELECT
    name
FROM SalesPerson
WHERE sales_id not in (
SELECT
distinct SP.sales_id
FROM SalesPerson SP
INNER JOIN Orders Ord
        ON Ord.sales_id = SP.sales_id
INNER JOIN Company Comp
        ON Comp.com_id = Ord.com_id
WHERE Comp.Name = 'RED'
)