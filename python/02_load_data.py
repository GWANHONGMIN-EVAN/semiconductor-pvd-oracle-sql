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
# 2. PVD 데이터 적재 함수
# ==========================

def load_pvd_data(material):

    print(f"{material} 데이터 적재 시작")


    # ==========================
    # 기존 RUN_ID 확인
    # ==========================

    cursor.execute(
        """
        SELECT NVL(MAX(run_id), 0)
        FROM pvd_run
        """
    )

    start_run_id = cursor.fetchone()[0]

    print("현재 마지막 RUN_ID :", start_run_id)


    # ==========================
    # X 데이터 읽기
    # ==========================

    x_file_path = f"../data/raw/X_pvd_{material}.csv"

    df = pd.read_csv(x_file_path)

    print("X 데이터 로드 완료")


    # ==========================
    # PVD_RUN 입력
    # ==========================

    run_data = []


    for idx in range(len(df)):

        run_id = start_run_id + idx + 1

        run_data.append(
            (
                run_id,
                material,
                idx + 1
            )
        )


    cursor.executemany(
        """
        INSERT INTO pvd_run
        (
            run_id,
            material_type,
            source_row_no
        )
        VALUES
        (
            :1,
            :2,
            :3
        )
        """,
        run_data
    )


    print("PVD_RUN 입력 완료")


    # ==========================
    # SENSOR 데이터 입력
    # ==========================

    sensor_data = []


    for idx, row in df.iterrows():

        run_id = start_run_id + idx + 1


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
    # Y 데이터 읽기
    # ==========================

    y_file_path = f"../data/raw/Y_pvd_{material}.csv"

    df_y = pd.read_csv(y_file_path)

    print("Y 데이터 로드 완료")


    # ==========================
    # THICKNESS 데이터 입력
    # ==========================

    thickness_data = []


    for idx, row in df_y.iterrows():

        run_id = start_run_id + idx + 1


        for point_no, value in enumerate(row, start=1):

            thickness_data.append(
                (
                    run_id,
                    point_no,
                    value
                )
            )


    cursor.executemany(
        """
        INSERT INTO thickness_measurement
        (
            run_id,
            measurement_point,
            thickness_value
        )
        VALUES
        (
            :1,
            :2,
            :3
        )
        """,
        thickness_data
    )


    print("THICKNESS_MEASUREMENT 입력 완료")



# ==========================
# 3. 데이터 적재 실행
# ==========================

# 이미 AlCu 데이터가 있으므로 WTi만 실행
load_pvd_data("WTi")


# ==========================
# 4. 저장
# ==========================

connection.commit()

cursor.close()
connection.close()

print("전체 데이터 입력 완료")
