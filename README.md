# 전력사용량 예측 프로젝트

XGBoost를 활용한 전력사용량 예측 모델입니다.

## 프로젝트 구조

```
elec_2025/
├── elec_2025_data/          # 데이터 폴더
│   ├── train.csv            # 학습 데이터
│   ├── test.csv             # 테스트 데이터
│   ├── building_info.csv    # 건물 정보
│   └── sample_submission.csv # 제출 샘플
├── electricity_prediction.py # 메인 실행 파일
├── requirements.txt         # 필요 패키지 목록
└── README.md               # 프로젝트 설명
```

## 설치 방법

### 1. Python 가상 환경 생성 (선택사항)

```bash
python -m venv .venv
```

### 2. 가상 환경 활성화

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 3. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

## 사용 방법

### 모델 학습 및 예측 실행

```bash
python electricity_prediction.py
```

실행하면 다음과 같은 과정이 진행됩니다:
1. 데이터 로드 (`elec_2025_data/train.csv`, `elec_2025_data/test.csv`)
2. 시계열 특성 추출 (월, 일, 시간)
3. XGBoost 모델 학습
4. 테스트 데이터 예측
5. 결과 저장 (`baseline_submission.csv`)

## 주요 기능

- **시계열 특성 추출**: 일시 데이터를 월, 일, 시간으로 분리하여 학습에 활용
- **XGBoost 모델**: 전력소비량 예측을 위한 gradient boosting 알고리즘 사용
- **재현성 보장**: Random seed 고정으로 동일한 결과 재현 가능

## 데이터 설명

- **train.csv**: 학습용 전력사용량 데이터
- **test.csv**: 예측할 테스트 데이터
- **building_info.csv**: 건물 정보 (현재 미사용)
- **sample_submission.csv**: 제출 파일 형식

## 출력 파일

- **baseline_submission.csv**: 예측 결과가 담긴 제출 파일

## 필요 패키지

- pandas: 데이터 처리
- numpy: 수치 계산
- xgboost: 모델 학습
- scikit-learn: 머신러닝 유틸리티

## 문제 해결

### ImportError: sklearn needs to be installed

XGBoost가 scikit-learn을 필요로 합니다. 다음 명령어로 설치하세요:
```bash
pip install scikit-learn
```

### 데이터 파일을 찾을 수 없음

`elec_2025_data` 폴더가 프로젝트 루트 디렉토리에 있는지 확인하세요.

## 참고사항

- Random seed는 42로 고정되어 있습니다
- 일조(hr), 일사(MJ/m2) 특성은 학습에서 제외됩니다
- 생성된 `baseline_submission.csv` 파일을 제출하시면 됩니다
