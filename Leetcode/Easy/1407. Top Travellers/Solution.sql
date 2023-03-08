WITH pre_data as (
SELECT
    Usr.id
    , COALESCE(SUM(Rds.distance),0) as travelled_distance 
FROM Users Usr
LEFT JOIN Rides Rds
        ON Usr.id = Rds.user_id
GROUP BY Usr.id
)
SELECT
 Usr.name
 ,pre_data.travelled_distance
FROM pre_data 
INNER JOIN Users Usr
        ON Usr.id = pre_data.id 
ORDER BY travelled_distance DESC, name ASC
    