DELETE FROM Person
WHERE id in
(
   WITH data as 
    (
        SELECT id, rank() OVER(PARTITION BY email ORDER BY id) rnk
        FROM Person
    )
         SELECT id FROM data
         WHERE rnk > 1
    
)