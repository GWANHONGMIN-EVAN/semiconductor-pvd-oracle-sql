\# Semiconductor PVD Process Data Analysis using Oracle SQL



Python과 Oracle Database를 활용해 반도체 PVD 공정 데이터를 관계형 데이터베이스로 구축하고, Sensor 데이터와 Thickness 결과 데이터를 분석함.



공정 품질 특성 비교 및 주요 영향 Sensor 탐색 프로젝트.



\## 1. Project Overview



\### Objective

PVD 공정 데이터를 활용하여 아래 분석 수행.



\- 소재별 Thickness 특성 비교

\- Thickness 균일도 분석

\- Sensor와 Thickness 간 상관관계 분석



\### Dataset



|Data|Description|

|---|---|

|X\_pvd\_AlCu.csv|AlCu 공정 Sensor 데이터|

|Y\_pvd\_AlCu.csv|AlCu 공정 Thickness 데이터|

|X\_pvd\_WTi.csv|WTi 공정 Sensor 데이터|

|Y\_pvd\_WTi.csv|WTi 공정 Thickness 데이터|



\## 2. Tech Stack



|Category|Tool|

|---|---|

|Database|Oracle Database, SQL Developer|

|Processing|Python, Pandas|

|Visualization|Matplotlib|

|Environment|VS Code, GitHub|



\## 3. Data Pipeline



```

Raw CSV Data

&#x20;     ↓

Python(Pandas)

&#x20;     ↓

Oracle Database

&#x20;     ↓

SQL Analysis

```



Python 기반 ETL Pipeline을 구축하여 Raw 데이터를 Oracle Database에 적재하고 분석 환경 구성.



\## 4. Database Design



PVD 공정 데이터를 Run 기준으로 관리하기 위해 관계형 구조로 설계함.



```

&#x20;             PVD\_RUN

&#x20;                |

&#x20;     -----------------------

&#x20;     |                     |

&#x20;     ↓                     ↓

SENSOR\_MEASUREMENT  THICKNESS\_MEASUREMENT

```



|Table|Description|

|---|---|

|PVD\_RUN|공정 Run 및 소재 정보 관리|

|SENSOR\_MEASUREMENT|증착 과정 Sensor 데이터 저장|

|THICKNESS\_MEASUREMENT|증착 결과 Thickness 데이터 저장|



\## 5. Analysis Result



\### 5.1 Thickness Uniformity



Material별 Thickness Standard Deviation 비교.



|Material|Thickness STD|

|---|---:|

|AlCu|0.1126|

|WTi|0.1595|



!\[Thickness Uniformity](images/thickness\_uniformity.png)



\*\*Insight\*\*

\- AlCu 공정이 WTi 대비 낮은 Thickness STD를 보여 상대적으로 균일한 증착 특성을 확인함.



\### 5.2 Sensor Impact Analysis



Sensor 데이터와 Thickness 결과 간 상관관계를 분석하여 영향 가능성이 높은 Sensor 탐색.



\#### AlCu



!\[AlCu Sensor Correlation](images/sensor\_correlation\_AlCu.png)



\- Sensor\_40이 가장 높은 상관관계 확인

\- 특정 Sensor 단독보다 여러 Sensor가 복합적으로 영향을 주는 형태 확인



\#### WTi



!\[WTi Sensor Correlation](images/sensor\_correlation\_WTi.png)



\- Sensor\_88에서 높은 상관관계(0.72) 확인

\- Thickness 변화와 관련성이 높은 주요 공정 변수 후보로 판단



\## 6. Project Structure



```

semiconductor-pvd-oracle-sql



├── analysis

├── data

├── docs

├── images

├── python

├── sql

└── README.md

```



\## 7. Key Achievement



\- Python 기반 PVD 공정 데이터 ETL Pipeline 구축

\- Oracle Database 관계형 데이터 모델 설계

\- SQL 기반 Thickness 품질 분석 수행

\- Sensor-Thickness 상관분석을 통한 주요 공정 변수 탐색



\## 8. Future Improvement



\- Sensor 기반 이상 공정 탐지

\- 공정 조건별 추가 분석

\- Regression 기반 영향 변수 분석

