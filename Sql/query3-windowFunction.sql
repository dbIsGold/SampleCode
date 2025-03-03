-- Running total of revenue for first 15 days of March’2022 using window function
--  Sample of Window Function Over a period

SELECT DISTINCT
    co.orderdate ,
    SUM(round((coi.quantity * p.price) - ((coi.quantity * p.price) * cp.percentdiscount/100),2)) 
	OVER (ORDER BY orderdate) AS running_total
FROM
    customerorder co
LEFT JOIN customerorderitem coi ON co.customerorderid = coi.customerorderid
LEFT JOIN product p ON coi.productid = p.productid
LEFT JOIN coupon cp ON cp.couponid = co.couponid
ORDER BY orderdate;


