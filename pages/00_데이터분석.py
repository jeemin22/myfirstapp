import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="MBTI 문화/소비 성향 시각화", layout="wide")

# CSV 파일 로딩 (캐시 적용)
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("countriesMBTI_16types.csv")
        return df
    except FileNotFoundError:
        st.error("❌ 'countriesMBTI_16types.csv' 파일이 현재 폴더에 없습니다.")
        return None

# 데이터 불러오기
df = load_data()

if df is not None:
    # 데이터 전처리: long-format으로 변환
    df_melted = df.melt(id_vars=["Country"], var_name="MBTI", value_name="Proportion")

    # 제목 및 설명
    st.title("🌍 MBTI 기반 문화/소비 성향 시각화")
    st.markdown(
        """
        이 대시보드는 **MBTI 16유형 비율**에 따라 국가 간 문화적 차이와 소비 성향을 시각화합니다.  
        MBTI 데이터는 마케팅 전략, 콘텐츠 기획, 브랜드 메시지 설계 등 다양한 분야에 활용될 수 있어요.
        """
    )

    # 국가 선택
    country_list = df["Country"].unique().tolist()
    selected_countries = st.multiselect(
        "🔍 비교할 국가를 선택하세요 (최대 5개 추천)", country_list, default=["South Korea", "United States"]
    )

    if selected_countries:
        filtered_df = df_melted[df_melted["Country"].isin(selected_countries)]

        # Altair 시각화
        chart = alt.Chart(filtered_df).mark_bar().encode(
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
        st.info("📌 하나 이상의 국가를 선택해주세요!")

    # 하단 안내
    st.markdown("---")
    st.caption("© 2025 MBTI Explorer | 데이터를 통해 세계를 이해하다 🌐")
