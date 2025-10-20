import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io


DATA_PATH = 'data/50_Startups.csv'


def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def download_button(df: pd.DataFrame):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(label='CSV 파일 다운로드', data=csv, file_name='50_Startups_clean.csv', mime='text/csv')


def run_eda():
    st.header('EDA — 데이터 탐색')

    # 데이터 로드
    try:
        df = load_data()
    except Exception as e:
        st.error(f'데이터 로드 실패: {e}')
        return

    st.subheader('원본 데이터 미리보기')
    st.dataframe(df.head(15))

    st.subheader('데이터 정보')
    # 더 보기 쉬운 표로 데이터 정보를 보여줍니다.
    info_df = []
    for col in df.columns:
        dtype = df[col].dtype
        non_null = df[col].count()
        missing_count = df[col].isnull().sum()
        missing_ratio = missing_count / len(df)
        unique = df[col].nunique(dropna=True)
        info_df.append({
            'column': col,
            'dtype': str(dtype),
            'non_null_count': int(non_null),
            'missing_count': int(missing_count),
            'missing_ratio': f"{missing_ratio:.2%}",
            'unique_values': int(unique)
        })

    info_df = pd.DataFrame(info_df)
    st.dataframe(info_df.set_index('column'))

    # 원본 df.info() 출력은 expander에 보관
    with st.expander('Raw df.info() 출력 보기'):
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    st.subheader('기술 통계 (수치형)')
    st.write(df.describe())

    # 결측치 및 중복
    st.subheader('결측치 및 중복 확인')
    missing = df.isnull().sum()
    st.write(missing)
    st.write(f'중복 행 수: {df.duplicated().sum()}')

    # 변수 타입
    st.subheader('변수 타입')
    st.write(df.dtypes)

    # 분포도 (히스토그램) - 수치형
    numeric = df.select_dtypes(include=['number'])
    st.subheader('수치형 변수 분포')
    cols = numeric.columns.tolist()
    for c in cols:
        fig, ax = plt.subplots(figsize=(6, 3))
        sns.histplot(df[c], kde=True, ax=ax)
        ax.set_title(f'{c} 분포')
        st.pyplot(fig)

    # 박스플롯(이상치 탐지)
    st.subheader('박스플롯 (이상치)')
    fig2, axes = plt.subplots(nrows=1, ncols=len(cols), figsize=(4 * len(cols), 4))
    if len(cols) == 1:
        axes = [axes]
    for ax, c in zip(axes, cols):
        sns.boxplot(y=df[c], ax=ax)
        ax.set_title(c)
    st.pyplot(fig2)

    # 상관관계 및 히트맵
    st.subheader('상관관계 히트맵')
    corr = numeric.corr()
    fig3, ax3 = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', ax=ax3, linewidths=1)
    st.pyplot(fig3)

    # State별 요약
    if 'State' in df.columns:
        st.subheader('State별 요약 통계')
        st.write(df.groupby('State').agg({'Profit': ['mean', 'median', 'count'],
                                          'R&D Spend': ['mean'],
                                          'Marketing Spend': ['mean']}))

    # 산점도 매트릭스 (작으면 pairplot)
    st.subheader('산점도 매트릭스 (pairplot)')
    try:
        fig4 = sns.pairplot(df.select_dtypes(include=['number']))
        st.pyplot(fig4.fig)
    except Exception as e:
        st.warning(f'pairplot 생성 중 오류: {e}')

    # 다운로드
    st.subheader('데이터 다운로드')
    download_button(df)

    st.success('EDA가 완료되었습니다.')
