\# PVD Database Design



\## 1. Database Overview



본 프로젝트에서는 PVD(Physical Vapor Deposition) 공정 데이터를 효율적으로 관리하고 분석하기 위해 Oracle Database를 활용하였다.



원본 CSV 데이터는 공정 정보, Sensor 측정값, Thickness 결과값이 분리되어 있지 않은 형태였기 때문에, 분석 목적에 맞게 관계형 데이터베이스 구조로 설계하였다.



Database Structure:



```

&#x20;                PVD\_RUN

&#x20;                   |

&#x20;       --------------------------

&#x20;       |                        |

&#x20;       ↓                        ↓

SENSOR\_MEASUREMENT     THICKNESS\_MEASUREMENT

```





\---



\# 2. Table Description





\## 2.1 PVD\_RUN



\### Purpose



하나의 PVD 증착 공정(Run)에 대한 기본 정보를 관리하는 Master Table이다.



각 공정마다 RUN\_ID를 부여하여 Sensor 데이터와 Thickness 결과 데이터를 연결하는 기준 테이블 역할을 한다.





\### Columns



| Column | Description |

|---|---|

| RUN\_ID | 공정 식별 번호 (Primary Key) |

| MATERIAL\_TYPE | 증착 소재 종류 (AlCu, WTi) |

| SOURCE\_ROW\_NO | 원본 CSV 데이터 행 번호 |





\### Example



|RUN\_ID|MATERIAL\_TYPE|SOURCE\_ROW\_NO|

|-|-|-|

|1|AlCu|1|

|2|AlCu|2|

|4849|WTi|1|





\---



\# 2.2 SENSOR\_MEASUREMENT



\### Purpose



PVD 증착 과정 중 장비 Sensor에서 측정된 공정 데이터를 저장한다.



원본 X 데이터에 해당하며, 증착 과정에서 발생하는 장비 상태 정보를 관리한다.





\### Columns



| Column | Description |

|---|---|

| RUN\_ID | 공정 식별 번호 |

| SENSOR\_NO | Sensor 번호 |

| SENSOR\_VALUE | Sensor 측정값 |





\### Example



|RUN\_ID|SENSOR\_NO|SENSOR\_VALUE|

|-|-|-|

|1|1|0.109237|

|1|2|0.234964|

|1|3|0.354292|





\### Interpretation



예를 들어:



RUN\_ID = 1, SENSOR\_NO = 25



이면:



"1번째 PVD 공정에서 25번 Sensor가 측정한 값"



을 의미한다.





\---



\# 2.3 THICKNESS\_MEASUREMENT



\### Purpose



증착 완료 후 측정된 박막 Thickness 결과 데이터를 저장한다.



원본 Y 데이터에 해당하며, 공정 결과 품질 지표를 관리한다.





\### Columns



| Column | Description |

|---|---|

| RUN\_ID | 공정 식별 번호 |

| MEASUREMENT\_POINT | Thickness 측정 위치 |

| THICKNESS\_VALUE | 측정된 Thickness 값 |





\### Example



|RUN\_ID|MEASUREMENT\_POINT|THICKNESS\_VALUE|

|-|-|-|

|1|1|0.612|

|1|2|0.623|

|1|3|0.598|





\---



\# 3. Relationship Between Tables



테이블 관계:



```

PVD\_RUN

&#x20;  |

&#x20;  | 1:N

&#x20;  |

&#x20;  ├── SENSOR\_MEASUREMENT



&#x20;  |

&#x20;  | 1:N

&#x20;  |

&#x20;  └── THICKNESS\_MEASUREMENT

```





하나의 RUN은:



\- 여러 개의 Sensor 측정값을 가짐

\- 여러 위치의 Thickness 측정값을 가짐





따라서 RUN\_ID를 Foreign Key로 활용하여 공정 조건과 결과 품질 간 관계 분석이 가능하도록 설계하였다.





\---



\# 4. Design Purpose



본 데이터 모델은 다음 분석을 가능하게 한다.



1\. 소재별 Thickness 특성 비교



```

Material

&#x20;   ↓

Thickness

```



2\. 공정 Sensor와 품질 결과 관계 분석



```

Sensor Value

&#x20;     ↓

Thickness

```



3\. 향후 이상 공정 탐지 및 공정 최적화 분석



```

Process Condition

&#x20;     ↓

Quality Result

```





\---



\# 5. Design Summary



PVD 공정 데이터를 Run 중심의 관계형 구조로 정규화하여,



\- 공정 정보 관리

\- Sensor 데이터 관리

\- 품질 결과 관리



를 분리하였다.



이를 통해 Oracle Database 기반으로 대규모 공정 데이터를 효율적으로 저장하고 SQL 기반 분석이 가능한 환경을 구축하였다.

