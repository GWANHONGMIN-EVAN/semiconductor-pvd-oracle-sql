import oracledb

connection = oracledb.connect(
    user="pvd_user",
    password="project",
    dsn="localhost:1521/freepdb1"
)

print("Oracle 연결 성공")

connection.close()