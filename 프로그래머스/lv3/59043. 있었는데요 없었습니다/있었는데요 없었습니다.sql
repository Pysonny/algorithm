-- 코드를 입력하세요
SELECT
    I.ANIMAL_ID , I.NAME 
FROM
    ANIMAL_INS AS I
INNER JOIN
    ANIMAL_OUTS AS O
USING
    (ANIMAL_ID)
WHERE
    I.DATETIME > O.DATETIME AND
    I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY
    I.DATETIME