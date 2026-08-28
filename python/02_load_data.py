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

cursor = connection.cursor()

print("Oracle 연결 성공")


# ==========================
# 2. CSV 읽기
# ==========================

file_path = "../data/raw/X_pvd_AlCu.csv"

df = pd.read_csv(file_path)

print("CSV 로드 완료")
print(df.head())


# ==========================
# 3. PVD_RUN 데이터 생성
# ==========================

material = "AlCu"

run_data = []

for idx in range(len(df)):
    run_data.append(
        (
            material,
            idx + 1
        )
    )


cursor.executemany(
    """
    INSERT INTO pvd_run
    (
        material_type,
        source_row_no
    )
    VALUES
    (
        :1,
        :2
    )
    """,
    run_data
)


print("PVD_RUN 입력 완료")


# ==========================
# 4. SENSOR 데이터 변환
# ==========================

sensor_data = []


for idx, row in df.iterrows():

    run_id = idx + 1

    for sensor_no, value in enumerate(row, start=1):

        sensor_data.append(
            (
                run_id,
                sensor_no,
                value
            )
        )


cursor.executemany(
    """
    INSERT INTO sensor_measurement
    (
        run_id,
        sensor_no,
        sensor_value
    )
    VALUES
    (
        :1,
        :2,
        :3
    )
    """,
    sensor_data
)


print("SENSOR_MEASUREMENT 입력 완료")


# ==========================
# 5. 저장
# ==========================

connection.commit()

cursor.close()
connection.close()

print("완료")