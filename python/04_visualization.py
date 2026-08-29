import pandas as pd
import matplotlib.pyplot as plt


# ==========================
# 1. Thickness Uniformity 시각화
# ==========================

material = [
    "AlCu",
    "WTi"
]

thickness_std = [
    0.1126,
    0.1595
]


plt.figure(figsize=(6,4))

plt.bar(
    material,
    thickness_std
)

plt.title(
    "Thickness Uniformity by Material"
)

plt.xlabel(
    "Material"
)

plt.ylabel(
    "Thickness STD"
)

plt.tight_layout()


plt.savefig(
    "../images/thickness_uniformity.png",
    dpi=300
)

plt.close()


print("Thickness Uniformity 그래프 저장 완료")



# ==========================
# 2. Sensor Correlation 시각화 함수
# ==========================


def create_sensor_chart(material):

    file_path = (
        f"../analysis/"
        f"sensor_correlation_{material}.csv"
    )


    df = pd.read_csv(
        file_path
    )


    # TOP 10
    df = df.head(10)


    # Sensor 이름 변경
    df["sensor_name"] = (
        "Sensor_"
        +
        df["sensor_no"].astype(str)
    )


    plt.figure(figsize=(8,5))


    plt.barh(
        df["sensor_name"],
        df["correlation"]
    )


    plt.title(
        f"{material} Sensor Correlation TOP 10"
    )


    plt.xlabel(
        "Correlation"
    )


    plt.ylabel(
        "Sensor"
    )


    plt.gca().invert_yaxis()


    plt.tight_layout()


    plt.savefig(
        f"../images/"
        f"sensor_correlation_{material}.png",
        dpi=300
    )


    plt.close()


    print(
        f"{material} Sensor 영향도 그래프 저장 완료"
    )



# ==========================
# 3. 소재별 Sensor 그래프 생성
# ==========================


create_sensor_chart("AlCu")

create_sensor_chart("WTi")


print(
    "전체 시각화 완료"
)
