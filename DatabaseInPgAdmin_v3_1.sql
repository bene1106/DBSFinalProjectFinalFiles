SELECT R.Region, 
    CAST(SUM(H.Anzahl_Studierende) AS DECIMAL(18,2)) * 100000 / NULLIF(AVG(r.maennlich) + AVG(r.weiblich), 0) AS Studirate
FROM Hochschule H
JOIN Ort O ON H.Ort = O.Ort
JOIN Region R ON O.Region = R.Region
GROUP BY R.Region
ORDER BY Studirate DESC;
