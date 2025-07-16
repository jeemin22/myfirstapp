import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="MBTI 문화/소비 성향 시각화", layout="wide")

# 파일 자동 로딩
@st.cache
def load_data():
    try:
        df = pd.read_csv("countriesMBTI_16types.csv")
        return df
    except FileNotFoundError:
        st.error("❌ 'countriesMBTI_16types.csv' 파일이 현재 폴더에 없습니다.")
        return None

df = load_data()

if df is not None:
    # 데이터 전처리
    df_melted = df.melt(id_vars=["Country"], var_name="MBTI", value_name="Proportion")

    # 제목 및 설명
    st.title("🌍 MBTI 기반 문화/소비 성향 시각화")
    st.markdown(
        "이 대시보드는 **MBTI 16유형 비율에 따른 국가 간 문화/소비 성향 차이**를 시각화합니다. "
        "국가별 MBTI 분포는 브랜드 메시지, 마케팅 전략, 소비 트렌드 연구에 활용될 수 있어요. ✨"
    )

    # 국가 선택 UI
    countries = df["Country"].unique().tolist()
    selected = st.multiselect("🔍 비교할 국가를 선택하세요:", countries, default=["South Korea", "United States"])

    if selected:
        filtered = df_melted[df_melted["Country"].isin(selected)]

        # Altair 그래프 생성
        chart = alt.Chart(filtered).mark_bar().encode(
            x=alt.X("MBTI:N", sort="y"),
            y=alt.Y("Proportion:Q", title="비율"),
            color="Country:N",
            column=alt.Column("Country:N", title=None)
        ).properties(height=300).configure_axis(
            labelFontSize=12,
            titleFontSize=14
        )

        st.altair_chart(chart, use_container_width=True)

    else:
        st.info("📌 국가를 하나 이상 선택해 주세요.")

    # 참고 문구
    st.markdown("---")
    st.caption("© 2025 MBTI Explorer | 데이터 기반 인사이트로 세계를 읽다.")
