SELECT  PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM    FOOD_PRODUCT
ORDER   BY PRICE DESC
FETCH   NEXT 1 ROW ONLY;