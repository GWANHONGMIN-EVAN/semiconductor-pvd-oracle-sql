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
# 2. 데이터 조회
# ==========================

query = """
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
    s.sensor_value
"""


df = pd.read_sql(
    query,
    connection
)


print("데이터 조회 완료")
print(df.head())


# ==========================
# 3. 소재별 Sensor 상관분석
# ==========================

materials = df["MATERIAL_TYPE"].unique()


for material in materials:

    print("\n====================")
    print(material)
    print("====================")


    material_df = df[
        df["MATERIAL_TYPE"] == material
    ]


    correlation_result = []


    for sensor_no, group in material_df.groupby("SENSOR_NO"):

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


    result_df["abs_correlation"] = (
        result_df["correlation"]
        .abs()
    )


    result_df = result_df.sort_values(
        by="abs_correlation",
        ascending=False
    )


    print("Sensor 영향도 TOP 10")

    print(
        result_df.head(10)
    )


    # 저장

    result_df.to_csv(
        f"../analysis/sensor_correlation_{material}.csv",
        index=False
    )


print("\n소재별 Sensor 분석 완료")
