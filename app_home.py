import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df


def run_home():
    st.header('홈 — 프로젝트 개요')

    st.markdown(
        """
        ### 스타트업 수익 예측 앱

        이 앱은 `data/50_Startups.csv` 데이터셋을 사용하여 스타트업의 수익(Profit)을 예측합니다.

        - 데이터 로드 및 간단한 탐색(EDA)
        - 주요 변수 시각화
        - 학습된 머신러닝 모델을 통한 예측 인터페이스는 `ML` 탭에서 제공합니다.
        """
    )

    # 데이터 로드
    try:
        df = load_data('data/50_Startups.csv')
    except Exception as e:
        st.error(f'데이터를 불러오는 중 오류가 발생했습니다: {e}')
        return

    st.subheader('데이터 미리보기')
    st.dataframe(df.head(10))

    st.subheader('데이터 요약')
    st.write(df.describe(include='all'))

    # 간단한 값 카운트(범주형)
    if 'State' in df.columns:
        st.subheader('State 분포')
        st.bar_chart(df['State'].value_counts())

    # 산점도: R&D Spend vs Profit
    if 'R&D Spend' in df.columns and 'Profit' in df.columns:
        st.subheader('R&D Spend vs Profit')
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x='R&D Spend', y='Profit', hue='State', palette='Set2', ax=ax)
        ax.set_xlabel('R&D Spend')
        ax.set_ylabel('Profit')
        st.pyplot(fig)

    # 상관계수
    st.subheader('수치형 변수 상관계수')
    numeric = df.select_dtypes(include=['number'])
    corr = numeric.corr()
    fig2, ax2 = plt.subplots()
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='Blues', ax=ax2, linewidths=1)
    st.pyplot(fig2)

    st.info('다음: 사이드바에서 `ML` 탭을 선택하면 모델 학습 및 예측 인터페이스로 이동합니다.')
