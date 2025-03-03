-- List total quantity of pizzas ordered by customers from most to least quantity
-- Sample of GroupBy, Having and OrderBy query

SELECT p.productname, SUM(coi.quantity) AS total_qty_ordered
FROM product p
LEFT JOIN  customerorderitem coi ON coi.productid = p.productid
GROUP BY 1
HAVING p.productname LIKE '%Pizza'
ORDER BY 2 DESC;

