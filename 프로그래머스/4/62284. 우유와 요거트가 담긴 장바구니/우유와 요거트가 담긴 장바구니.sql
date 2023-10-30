SELECT  DISTINCT C1.CART_ID
FROM    CART_PRODUCTS C1, CART_PRODUCTS C2
WHERE   C1.CART_ID = C2.CART_ID
        AND C1.NAME = 'Milk'
        AND C2.NAME = 'Yogurt'
ORDER   BY C1.CART_ID