USE quiz;
GO

SELECT * FROM t_ma WHERE ort = 'Berlin' OR 'Hamburg'

SELECT * FROM t_ma WHERE ort = 'Berlin' OR ort = 'Hamburg';