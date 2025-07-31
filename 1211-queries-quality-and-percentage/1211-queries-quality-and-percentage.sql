SELECT query_name,
       round(AVG(rating::numeric/position), 2) AS quality,
       round(100 * SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END)::numeric / COUNT(*), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;
