SELECT  C.CAR_ID, C.CAR_TYPE, (SELECT  1 - DISCOUNT_RATE / 100
        FROM    CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
        WHERE   DURATION_TYPE = '30일 이상'
                AND C.CAR_TYPE = P.CAR_TYPE
                AND C.CAR_TYPE IN ('세단', 'SUV')) * DAILY_FEE * 30 AS FEE
FROM    CAR_RENTAL_COMPANY_CAR C
WHERE   (SELECT  1 - DISCOUNT_RATE / 100
        FROM    CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
        WHERE   DURATION_TYPE = '30일 이상'
                AND C.CAR_TYPE = P.CAR_TYPE
                AND C.CAR_TYPE IN ('세단', 'SUV')) * DAILY_FEE * 30 BETWEEN 500000 AND 2000000
        AND C.CAR_ID IN (SELECT  C2.CAR_ID
                        FROM    CAR_RENTAL_COMPANY_CAR C2
                        MINUS
                        SELECT  H.CAR_ID
                        FROM    CAR_RENTAL_COMPANY_RENTAL_HISTORY H
                        WHERE   TO_CHAR(H.START_DATE, 'YYYY-MM') <= '2022-11'
                                AND TO_CHAR(H.END_DATE, 'YYYY-MM') >= '2022-11')
ORDER   BY FEE DESC, C.CAR_TYPE ASC, C.CAR_ID DESC;