-- Write your query below
SELECT 
    c.customer_id,
    c.customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.product_name = 'A' and o.customer_id = c.customer_id
)
AND EXISTS(
    SELECT 1
    FROM orders o
    WHERE o.product_name = 'B' and o.customer_id = c.customer_id
)
AND NOT EXISTS(
    SELECT 1
    FROM orders o
    WHERE o.product_name = 'C' and o.customer_id = c.customer_id
)
ORDER BY c.customer_name;
