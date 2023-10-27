SELECT  BOARD_ID, WRITER_ID, TITLE, PRICE, DECODE (STATUS, 'DONE', '거래완료',
                                                   'SALE', '판매중',
                                                   'RESERVED', '예약중') AS STATUS
FROM    USED_GOODS_BOARD
WHERE   TO_CHAR(CREATED_DATE, 'YYYY-MM-DD') = '2022-10-05'
ORDER   BY BOARD_ID DESC;