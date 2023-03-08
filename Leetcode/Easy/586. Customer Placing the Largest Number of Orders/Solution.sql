WITH customers_cnt_orders as (
SELECT
 customer_number, COUNT(order_number) as cnt_orders
FROM Orders
GROUP BY customer_number
)
SELECT
    customer_number
FROM customers_cnt_orders
WHERE cnt_orders = (SELECT MAX(cnt_orders) FROM customers_cnt_orders)