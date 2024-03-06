SELECT  P.PRODUCT_ID, P.PRODUCT_NAME, P.PRICE * O.AMOUNT TOTAL_SALES
FROM    FOOD_PRODUCT P
INNER   JOIN (SELECT  PRODUCT_ID, SUM(AMOUNT) AS AMOUNT
            FROM    FOOD_ORDER
            WHERE   TO_CHAR(PRODUCE_DATE, 'YYYY-MM') = '2022-05'
            GROUP BY  PRODUCT_ID) O
ON      P.PRODUCT_ID = O.PRODUCT_ID
ORDER   BY 3 DESC, 1 ASC;