-- Write your query below
SELECT C.name
FROM customers C
where C.id NOT IN (
    SELECT customer_id
    FROM orders
)