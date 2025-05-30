SELECT DISTINCT CC.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR AS CC
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS CRH ON CC.CAR_ID = CRH.CAR_ID
WHERE CC.CAR_TYPE = '세단'
    AND MONTH(CRH.START_DATE) = 10
ORDER BY CC.CAR_ID DESC