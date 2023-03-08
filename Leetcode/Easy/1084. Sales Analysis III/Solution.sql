SELECT
    Pr.product_id   
    ,Pr.product_name
FROM Product Pr
INNER JOIN Sales
        ON Pr.product_id = Sales.product_id
WHERE Sales.sale_date  between '2019-01-01' AND '2019-03-31'

MINUS

SELECT
    Pr.product_id   
    ,Pr.product_name
FROM Product Pr
INNER JOIN Sales
        ON Pr.product_id = Sales.product_id
WHERE Sales.sale_date not between '2019-01-01' AND '2019-03-31'
