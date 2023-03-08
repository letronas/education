WITH pre_data as 
(
    SELECT 
        distinct author_id, viewer_id
    FROM Views
    WHERE author_id = viewer_id
)
SELECT 
    distinct author_id as id
FROM pre_data
ORDER BY author_id