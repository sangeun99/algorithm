SELECT  H.HISTORY_ID, CASE WHEN (END_DATE - START_DATE + 1) >=7 THEN (END_DATE - START_DATE + 1) * ( SELECT  DAILY_FEE
                    FROM    CAR_RENTAL_COMPANY_CAR  C
                    WHERE   C.CAR_ID = H.CAR_ID) * (1 - (SELECT  DISCOUNT_RATE
        FROM    CAR_RENTAL_COMPANY_DISCOUNT_PLAN
        WHERE   CAR_TYPE = '트럭'
                AND DURATION_TYPE = CASE WHEN (END_DATE - START_DATE + 1) >= 90 THEN '90일 이상'
                                WHEN (END_DATE - START_DATE + 1) >= 30 THEN '30일 이상'
                                WHEN (END_DATE - START_DATE + 1) >= 7 THEN '7일 이상' END) / 100) 
                    ELSE (END_DATE - START_DATE + 1) * ( SELECT  DAILY_FEE
                    FROM    CAR_RENTAL_COMPANY_CAR  C
                    WHERE   C.CAR_ID = H.CAR_ID) END AS FEE
FROM    CAR_RENTAL_COMPANY_RENTAL_HISTORY H
WHERE   CAR_ID IN ( SELECT  CAR_ID
                    FROM    CAR_RENTAL_COMPANY_CAR  
                    WHERE   CAR_TYPE = '트럭')        
ORDER   BY 2 DESC, 1 DESC;
