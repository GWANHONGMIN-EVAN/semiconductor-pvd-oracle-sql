Material별 데이터 개수

SELECT
    material_type,
    COUNT(*)
FROM pvd_run
GROUP BY material_type;

Thickness 데이터 확인

SELECT *
FROM thickness_measurement
FETCH FIRST 10 ROWS ONLY;


Sensor 데이터 확인

SELECT *
FROM sensor_measurement
FETCH FIRST 10 ROWS ONLY;

Thickness 적재 확인

SELECT 
    r.material_type,
    COUNT(*)
FROM thickness_measurement t
JOIN pvd_run r
ON t.run_id = r.run_id
GROUP BY r.material_type;