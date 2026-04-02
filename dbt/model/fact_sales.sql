SELECT
    product,
    SUM(amount) AS total_amount
FROM sales_data
GROUP BY product

