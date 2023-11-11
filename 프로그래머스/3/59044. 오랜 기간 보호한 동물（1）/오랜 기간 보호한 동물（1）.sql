SELECT  NAME, DATETIME
FROM    ANIMAL_INS
WHERE   ANIMAL_ID IN    (SELECT  ANIMAL_ID
                        FROM    ANIMAL_INS
                        MINUS
                        SELECT  ANIMAL_ID
                        FROM    ANIMAL_OUTS)
ORDER   BY DATETIME
FETCH   NEXT 3 ROWS ONLY;