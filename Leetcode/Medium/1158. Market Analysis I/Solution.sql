WITH pre_data as (
SELECT
    Usr.user_id
    ,COALESCE(SUM(CASE WHEN EXTRACT(YEAR FROM Ord.order_date) = 2019 THEN 1 ELSE 0 END),0) AS orders_in_2019
FROM Users Usr
LEFT JOIN Orders Ord
        ON Usr.user_id = Ord.buyer_id
GROUP BY Usr.user_id
)
SELECT
    Usr.user_id as buyer_id  
    ,Usr.join_date
    ,pre_data.orders_in_2019
FROM pre_data
INNER JOIN Users Usr
        ON Usr.user_id = pre_data.user_id
