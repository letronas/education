SELECT
product_id, lower(store) as store, price 
FROM Products
UNPIVOT EXCLUDE NULLS 
( 
    price FOR store IN (store1,store2,store3)
)
