# streamlit-50-startups

간단한 Streamlit 기반 웹앱으로, `data/50_Startups.csv` 데이터를 사용해 스타트업의 수익(Profit)을 탐색하고 예측하는 데모 프로젝트입니다.

## 주요 기능
- 홈: 프로젝트 개요와 데이터 미리보기, 기본 시각화 제공
- EDA: 상세 데이터 탐색(기술통계, 결측치/중복 확인, 분포도, 박스플롯, 상관관계, pairplot, State별 요약)
- ML: 머신러닝 모델을 사용한 수익 예측 인터페이스 (별도 모듈 `app_ml.py`)

## 요구사항
- Python 3.8 이상 권장
- 주요 라이브러리: streamlit, pandas, matplotlib, seaborn, scikit-learn (ML탭 사용 시)

간단한 설치(가상환경 권장):

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install streamlit pandas matplotlib seaborn scikit-learn
```

## 실행 방법

프로젝트 루트에서 다음을 실행하세요:

```bash
streamlit run app.py
```

앱이 로컬 브라우저에서 열리면 사이드바에서 `Home`, `EDA`, `ML` 탭을 선택하여 기능을 확인할 수 있습니다.

## 데이터
- 파일: `data/50_Startups.csv`
- 컬럼: `R&D Spend`, `Administration`, `Marketing Spend`, `State`, `Profit`

## 파일 구조

```
app.py           # 메인 라우터
app_home.py      # Home 페이지 렌더러
app_eda.py       # EDA 페이지 렌더러
app_ml.py        # ML 페이지(모델 학습/예측 로직)
data/50_Startups.csv
model/            # 학습된 모델 저장용(선택)
README.md
```

## 기여
- 간단한 기능 개선이나 버그 수정은 PR 환영합니다. 주요 변경사항은 README에 명시해주세요.

## 라이선스
- 특별한 라이선스가 지정되어 있지 않습니다. 개인/학습용으로 사용하세요.

---
프로젝트를 실행하거나 README에 추가할 내용을 원하시면 알려주세요.
