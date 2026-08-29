# \# Semiconductor PVD Process Data Analysis using Oracle SQL

# 

# Python과 Oracle Database를 활용하여 반도체 PVD(Physical Vapor Deposition) 공정 데이터를

# 관계형 데이터베이스로 구축하고, Sensor 데이터와 Thickness 결과 데이터를 분석하여

# 공정 품질 특성과 주요 영향 변수를 도출하는 프로젝트

# 

# 

# \---

# 

# \# 1. Project Overview

# 

# \## Objective

# 

# PVD 공정 과정에서 측정되는 Sensor 데이터(X)와

# 증착 완료 후 측정되는 Thickness 데이터(Y)를 활용하여

# 

# \- 소재별 박막 두께 특성 비교

# \- Thickness 균일도 분석

# \- Sensor와 Thickness 간 상관관계 분석

# 

# 을 수행

# 

# \---

# 

# \# 2. Tech Stack

# 

# \## Database

# 

# \- Oracle Database

# \- SQL Developer

# 

# 

# \## Data Processing

# 

# \- Python

# \- Pandas

# \- Matplotlib

# \- python-oracledb

# 

# 

# \## Development Environment

# 

# \- GitHub

# \- VS Code

# 

# 

# \---

# 

# \# 3. Dataset Structure

# 

# 사용 데이터:

# 

# | File | Description |

# |---|---|

# | X\_pvd\_AlCu.csv | AlCu 공정 Sensor 데이터 |

# | Y\_pvd\_AlCu.csv | AlCu 공정 Thickness 데이터 |

# | X\_pvd\_WTi.csv | WTi 공정 Sensor 데이터 |

# | Y\_pvd\_WTi.csv | WTi 공정 Thickness 데이터 |

# 

# 

# 데이터 구조:

# 

# ```

# Raw CSV Data

# 

# &#x20;       ↓

# 

# Python(Pandas)

# 

# &#x20;       ↓

# 

# Oracle Database

# 

# &#x20;       ↓

# 

# SQL Analysis

# ```

# 

# \---

# 

# \# 4. Database Design

# 

# Oracle Database 내에서 PVD 공정 데이터를 정규화하여 관리 - python 이용

# 

# \## Table Structure

# 

# ```

# PVD\_RUN

# 

# &#x20;   |

# 

# &#x20;   ├── SENSOR\_MEASUREMENT

# 

# &#x20;   |

# 

# &#x20;   └── THICKNESS\_MEASUREMENT

# ```

# 

# 

# \## PVD\_RUN

# 

# 공정 Run 정보 및 소재 정보 관리

# 

# 

# \## SENSOR\_MEASUREMENT

# 

# 증착 과정에서 측정된 Sensor 데이터 저장

# 

# 

# \## THICKNESS\_MEASUREMENT

# 

# 증착 완료 후 측정된 Thickness 결과 데이터 저장

# 

# 

# \---

# 

# \# 5. Data Pipeline

# 

# 

# \## Step 1. Data Loading

# 

# Python(Pandas)을 활용하여 Raw CSV 데이터를 읽고

# Oracle Database 적재를 위한 형태로 변환

# 

# 

# \## Step 2. Database Loading

# 

# Python과 Oracle 연결을 통해:

# 

# \- PVD\_RUN

# \- SENSOR\_MEASUREMENT

# \- THICKNESS\_MEASUREMENT

# 

# 테이블에 데이터를 적재

# 

# 

# \## Step 3. SQL Analysis

# 

# Oracle SQL을 활용하여 소재별 Thickness 특성 분석

# 

# 

# \---

# 

# \# 6. Analysis Result

# 

# 

# \## 6.1 Thickness Uniformity Analysis

# 

# 

# Material별 Thickness Standard Deviation 비교

# 

# 

# |Material|Thickness STD|

# |-|-|

# |AlCu|0.1126|

# |WTi|0.1595|

# 

# 

# !\[Thickness Uniformity](images/thickness\_uniformity.png)

# 

# 

# \### Insight

# 

# AlCu 공정은 WTi 대비 낮은 Thickness STD를 보여

# 상대적으로 균일한 박막 증착 특성을 나타냄

# 

# 

# 

# \---

# 

# \# 6.2 Sensor Impact Analysis

# 

# 

# Sensor 데이터와 Thickness 결과 간 상관관계를 분석하여

# 공정 영향 가능성이 높은 Sensor를 탐색

# 

# 

# \## AlCu

# 

# 

# !\[AlCu Sensor Correlation](images/sensor\_correlation\_AlCu.png)

# 

# 

# AlCu 공정에서는 Sensor\_40이 가장 높은 상관관계를 보였으나,

# 특정 Sensor 하나보다는 여러 Sensor가 복합적으로 영향을 주는 형태로 판단함. ( 상관계수 값 상대적으로 적음)

# 

# 

# \## WTi

# 

# 

# !\[WTi Sensor Correlation](images/sensor\_correlation\_WTi.png)

# 

# 

# WTi 공정에서는 Sensor\_88이 높은 상관관계를 보여

# Thickness 변화와 관련성이 높은 주요 공정 변수 후보로 확인됨 -> 앞으로의 공정 수정에 가중치 두어서 판단

# 

# 

# \---

# 

# \# 7. Project Structure

# 

# 

# ```

# semiconductor-pvd-oracle-sql

# 

# ├── analysis

# │   ├── sensor\_correlation\_AlCu.csv

# │   └── sensor\_correlation\_WTi.csv

# │

# ├── data

# │   └── raw dataset

# │

# ├── docs

# │   └── analysis\_result.md

# │

# ├── images

# │   ├── thickness\_uniformity.png

# │   ├── sensor\_correlation\_AlCu.png

# │   └── sensor\_correlation\_WTi.png

# │

# ├── python

# │   ├── 01\_check\_connection.py

# │   ├── 02\_load\_data.py

# │   ├── 03\_sensor\_analysis.py

# │   └── 04\_visualization.py

# │

# └── sql

# ```

# 

# 

# \---

# 

# \# 8. Future Improvement

# 

# 향후 개선 방향:

# 

# \- Sensor 데이터 기반 이상 공정 탐지

# \- 공정 조건별 추가 분석

# \- Regression 기반 영향 변수 분석

# 

# \---

# 

# \# 9. Key Achievement

# 

# \- Python 기반 데이터 전처리 및 Oracle Database 적재 Pipeline 구축

# \- 반도체 PVD 공정 데이터를 관계형 DB 구조로 설계

# \- SQL 기반 Thickness 품질 분석 수행

# \- Sensor와 Thickness 간 상관관계 분석을 통한 주요 공정 변수 탐색

