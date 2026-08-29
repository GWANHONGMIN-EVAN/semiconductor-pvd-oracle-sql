import pandas as pd
import oracledb


# ==========================
# 1. Oracle 연결
# ==========================

connection = oracledb.connect(
    user="pvd_user",
    password="project",
    dsn="localhost:1521/freepdb1"
)

print("Oracle 연결 성공")


# ==========================
# 2. 분석 데이터 조회
# ==========================

query = """
SELECT
    s.run_id,
    s.sensor_no,
    s.sensor_value,
    AVG(t.thickness_value) AS thickness_value
FROM sensor_measurement s
JOIN thickness_measurement t
ON s.run_id = t.run_id
GROUP BY
    s.run_id,
    s.sensor_no,
    s.sensor_value
"""


df = pd.read_sql(
    query,
    connection
)


print("데이터 조회 완료")
print(df.head())


# ==========================
# 3. Sensor별 상관관계 분석
# ==========================

correlation_result = []


for sensor_no, group in df.groupby("SENSOR_NO"):

    corr = group["SENSOR_VALUE"].corr(
        group["THICKNESS_VALUE"]
    )

    correlation_result.append(
        (
            sensor_no,
            corr
        )
    )


result_df = pd.DataFrame(
    correlation_result,
    columns=[
        "sensor_no",
        "correlation"
    ]
)


# 절대값 기준 정렬
result_df["abs_correlation"] = (
    result_df["correlation"]
    .abs()
)


result_df = result_df.sort_values(
    by="abs_correlation",
    ascending=False
)


print("\nSensor 영향도 TOP 10")

print(
    result_df.head(10)
)


# ==========================
# 4. 저장
# ==========================

result_df.to_csv(
    "../analysis/sensor_correlation.csv",
    index=False
)


print("\n분석 결과 저장 완료")
