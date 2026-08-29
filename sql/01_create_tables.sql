-- PVD_RUN Table 생성

CREATE TABLE pvd_run
(
    run_id NUMBER PRIMARY KEY,
    material_type VARCHAR2(20),
    source_row_no NUMBER
);


-- SENSOR_MEASUREMENT Table 생성

CREATE TABLE sensor_measurement
(
    run_id NUMBER,
    sensor_no NUMBER,
    sensor_value NUMBER,

    CONSTRAINT fk_sensor_run
    FOREIGN KEY(run_id)
    REFERENCES pvd_run(run_id)
);


-- THICKNESS_MEASUREMENT Table 생성

CREATE TABLE thickness_measurement
(
    run_id NUMBER,
    measurement_point NUMBER,
    thickness_value NUMBER,

    CONSTRAINT fk_thickness_run
    FOREIGN KEY(run_id)
    REFERENCES pvd_run(run_id)
);