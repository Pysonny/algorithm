-- 코드를 입력하세요
SELECT
    ANIMAL_INS.NAME , ANIMAL_INS.DATETIME
FROM
    ANIMAL_INS
INNER JOIN
    ANIMAL_OUTS
USING 
    (ANIMAL_ID)
WHERE
    ANIMAL_OUTS.ANIMAL_ID IS NOT NULL
ORDER BY
    ANIMAL_INS.DATETIME
LIMIT 3