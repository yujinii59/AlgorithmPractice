-- 코드를 입력하세요
SELECT CAR.CAR_ID
     , CAR.CAR_TYPE
     , ROUND(CAR.DAILY_FEE * DSCNT.RATE,0) * 30 FEE
  FROM (
            SELECT CAR_ID
                 , CAR_TYPE
                 , DAILY_FEE
              FROM CAR_RENTAL_COMPANY_CAR
             WHERE CAR_TYPE IN ('세단', 'SUV')
               AND CAR_ID NOT IN (
                                    SELECT CAR_ID
                                      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                                     WHERE START_DATE <= DATE_FORMAT('20221130', '%Y%m%d')
                                       AND END_DATE >= DATE_FORMAT('20221101', '%Y%m%d')
                                )
      ) CAR
 INNER JOIN (
                SELECT CAR_TYPE
                     , (100-DISCOUNT_RATE)/100 RATE
                  FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                 WHERE DURATION_TYPE = '30일 이상'
                   AND CAR_TYPE IN ('세단', 'SUV')
     ) DSCNT
    ON CAR.CAR_TYPE = DSCNT.CAR_TYPE
WHERE ROUND(CAR.DAILY_FEE * RATE,0) * 30 >= 500000 AND ROUND(CAR.DAILY_FEE * RATE,0) * 30 < 2000000
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC