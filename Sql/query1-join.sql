-- Get the order detail for order placed by customer on 4th March, 2022 by customer 'Duffy'
--  Sample of multi table join query

SELECT c.lastname, co.orderdate, coi.quantity, p.productname, (coi.quantity * p.price) AS prod_price,
round((coi.quantity * p.price) - ((coi.quantity * p.price) * cp.percentdiscount/100),2) AS discounted_price,  cp.coupondescription 
FROM customer c 
LEFT JOIN customerorder co ON c.customerid = co.customerid
LEFT JOIN customerorderitem coi ON co.customerorderid = coi.customerorderid
LEFT JOIN product p ON coi.productid = p.productid
LEFT JOIN coupon cp ON cp.couponid = co.couponid
WHERE c.lastname = 'Duffy' AND (co.orderdate) = TO_DATE('2022-03-04', 'YYYY-MM-DD');

