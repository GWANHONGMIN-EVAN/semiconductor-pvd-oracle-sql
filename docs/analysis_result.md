# PVD Process Data Analysis

## 1. Analysis Objective

본 프로젝트는 PVD(Physical Vapor Deposition) 공정 데이터를 활용하여  
공정 중 측정되는 Sensor 데이터(X)와 증착 완료 후 측정되는 박막 두께 데이터(Y)를 기반으로 소재별 공정 특성을 분석하는 것을 목적으로 한다.

X 데이터는 PVD 증착 과정에서 장비 Sensor를 통해 측정된 공정 데이터이며,  
Y 데이터는 증착 완료 후 측정된 박막 Thickness 결과 데이터이다.

분석 대상 소재:
- AlCu
- WTi


---

# 2. Data Structure

## Input Data

| File | Description |
|---|---|
| X_pvd_AlCu.csv | AlCu 증착 공정 Sensor 데이터 |
| Y_pvd_AlCu.csv | AlCu 증착 결과 Thickness 데이터 |
| X_pvd_WTi.csv | WTi 증착 공정 Sensor 데이터 |
| Y_pvd_WTi.csv | WTi 증착 결과 Thickness 데이터 |


## Oracle Database Structure

```
PVD_RUN
    |
    ├── SENSOR_MEASUREMENT
    |
    └── THICKNESS_MEASUREMENT
```


## Table Description

### PVD_RUN

공정 Run 정보와 소재 정보를 저장하는 테이블

| Column | Description |
|---|---|
| RUN_ID | 공정 식별 번호 |
| MATERIAL_TYPE | 증착 소재(AlCu, WTi) |
| SOURCE_ROW_NO | 원본 데이터 행 번호 |


### SENSOR_MEASUREMENT

PVD 증착 과정에서 측정된 Sensor 데이터를 저장하는 테이블

| Column | Description |
|---|---|
| RUN_ID | 공정 식별 번호 |
| SENSOR_NO | Sensor 번호 |
| SENSOR_VALUE | Sensor 측정값 |


### THICKNESS_MEASUREMENT

증착 완료 후 측정된 박막 두께 데이터를 저장하는 테이블

| Column | Description |
|---|---|
| RUN_ID | 공정 식별 번호 |
| MEASUREMENT_POINT | Thickness 측정 위치 |
| THICKNESS_VALUE | Thickness 측정값 |


---

# 3. Thickness Analysis

## 3.1 Material별 평균 Thickness 분석

### 목적

AlCu와 WTi 소재별 평균 박막 두께 특성을 비교한다.


### SQL

```sql
SELECT 
    r.material_type,
    AVG(t.thickness_value) AS avg_thickness
FROM thickness_measurement t
JOIN pvd_run r
ON t.run_id = r.run_id
GROUP BY r.material_type;
```


### Result

| Material | Average Thickness |
|---|---|
| AlCu | 0.612 |
| WTi | 0.734 |


### Analysis

WTi 공정의 평균 Thickness 값이 AlCu 대비 높게 나타났다.

다만 제공된 데이터는 정규화된 값으로 구성되어 있어 실제 nm 단위의 절대 두께가 아닌 소재별 상대 비교 기준으로 해석하였다.


---

# 4. Thickness Uniformity Analysis

## 4.1 Thickness Standard Deviation 분석


### 목적

박막 두께의 변동성을 확인하여 소재별 공정 균일도를 비교한다.

표준편차(Standard Deviation)가 낮을수록 동일 공정 내 Thickness 변화가 작아 안정적인 증착 특성을 의미한다.


### SQL

```sql
SELECT
    r.material_type,
    STDDEV(t.thickness_value) AS thickness_std
FROM thickness_measurement t
JOIN pvd_run r
ON t.run_id = r.run_id
GROUP BY r.material_type;
```


### Result

| Material | Thickness STD |
|---|---|
| AlCu | 0.1126 |
| WTi | 0.1595 |


### Analysis

AlCu 공정은 WTi 대비 낮은 Thickness Standard Deviation을 보였다.

따라서 현재 데이터 기준으로 AlCu 공정이 WTi 대비 상대적으로 균일한 박막 증착 특성을 보이는 것으로 판단된다.


---

# 5. Coefficient of Variation Analysis

## 목적

평균 Thickness 대비 상대적인 변동성을 비교하기 위해 CV(Coefficient of Variation)를 계산한다.

```
CV = Standard Deviation / Average Thickness
```


### SQL

```sql
SELECT
    r.material_type,
    AVG(t.thickness_value) AS avg_thickness,
    STDDEV(t.thickness_value) AS thickness_std,
    STDDEV(t.thickness_value) / AVG(t.thickness_value) AS cv
FROM thickness_measurement t
JOIN pvd_run r
ON t.run_id = r.run_id
GROUP BY r.material_type;
```


### Analysis

CV를 통해 평균 Thickness 대비 변동성을 확인하여 소재별 상대적인 공정 안정성을 평가할 수 있다.


---

# 6. Analysis Insight

- Python(Pandas)과 Oracle Database를 활용하여 PVD 공정 Raw 데이터를 분석 가능한 관계형 데이터 구조로 구축하였다.

- CSV 형태의 원본 데이터를 Python을 통해 전처리하고 Sensor 데이터와 Thickness 데이터를 Oracle Database에 적재하는 ETL Pipeline을 구축하였다.

- AlCu와 WTi 소재별 Thickness 특성을 비교한 결과, AlCu 공정은 WTi 대비 낮은 Thickness Standard Deviation을 보여 상대적으로 안정적인 증착 특성을 나타냈다.

- WTi 공정은 Thickness 변동성이 상대적으로 높게 나타났으며, Sensor 데이터와 Thickness 결과 간 관계 분석을 통해 추가적인 공정 영향 변수 확인이 필요하다.

- 본 분석 결과를 기반으로 향후 Sensor별 영향도 분석 및 이상 공정 탐지를 수행할 예정이다.

