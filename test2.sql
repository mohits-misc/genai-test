SELECT * FROM sales_data WHERE region = 'North' OR region = 'South' OR region = 'East' OR region = 'West';

SELECT *
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
WHERE orders.order_date > '2020-01-01';


SELECT SUM(total_amount)
FROM orders
WHERE order_date > '2020-01-01';