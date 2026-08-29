평균 Thickness

SELECT
    r.material_type,
    AVG(t.thickness_value) AS avg_thickness
FROM thickness_measurement t
JOIN pvd_run r
ON t.run_id = r.run_id
GROUP BY r.material_type;

Thickness 편차

SELECT
    r.material_type,
    STDDEV(t.thickness_value) AS thickness_std
FROM thickness_measurement t
JOIN pvd_run r
ON t.run_id = r.run_id
GROUP BY r.material_type;


Sensor 분석용 데이터 추출

SELECT
    r.material_type,
    s.run_id,
    s.sensor_no,
    s.sensor_value,
    AVG(t.thickness_value) AS thickness_value
FROM sensor_measurement s
JOIN thickness_measurement t
ON s.run_id = t.run_id
JOIN pvd_run r
ON s.run_id = r.run_id
GROUP BY
    r.material_type,
    s.run_id,
    s.sensor_no,
    s.sensor_value;