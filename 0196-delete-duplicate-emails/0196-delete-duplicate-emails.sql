DELETE
FROM Person
WHERE id IN 
    (SELECT p1.id
    FROM Person p1
    JOIN Person p2
        ON p1.email = p2.email
    WHERE p1.id != p2.id
            AND LEAST(p1.id, p2.id) < p1.id);