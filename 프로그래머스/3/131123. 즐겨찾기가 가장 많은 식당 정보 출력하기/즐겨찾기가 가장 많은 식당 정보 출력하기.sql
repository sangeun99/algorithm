SELECT  R1.FOOD_TYPE, R1.REST_ID, R1.REST_NAME, R1.FAVORITES
FROM    REST_INFO R1
WHERE   (R1.FOOD_TYPE, R1.FAVORITES) IN (SELECT  FOOD_TYPE, MAX(FAVORITES) FAVORITES
                                        FROM    REST_INFO R2
                                        GROUP   BY FOOD_TYPE)
ORDER   BY R1.FOOD_TYPE DESC;