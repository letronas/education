WITH pre_data as (
SELECT
t1.id, t1.p_id, COUNT(t2.id) as cnt_leafs
FROM Tree t1
LEFT JOIN Tree t2
    on t1.id = t2.p_id
GROUP BY t1.id, t1.p_id
)
SELECT
id
,
CASE 
    WHEN p_id IS NOT NULL AND cnt_leafs <> 0 THEN 'Inner'
    WHEN p_id IS NOT NULL AND cnt_leafs = 0 THEN 'Leaf'
    ELSE 'Root'
END as type
FROM pre_data