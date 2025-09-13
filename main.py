import streamlit as st
import pandas as pd
import altair as alt
import os

st.set_page_config(page_title="MBTI 국가 분석", layout="wide")

st.title("🌍 국가별 MBTI 유형 분석")
st.write("CSV 데이터를 기반으로 MBTI 유형별 비율이 가장 높은 상위 10개 국가를 확인할 수 있습니다.")

# 기본 파일 경로
default_file = "countriesMBTI_16types.csv"

# 데이터 불러오기 함수
def load_data():
    if os.path.exists(default_file):
        st.success(f"기본 데이터 파일 **{default_file}** 을(를) 불러왔습니다.")
        return pd.read_csv(default_file)
    else:
        uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])
        if uploaded_file is not None:
            st.success("업로드한 파일을 불러왔습니다.")
            return pd.read_csv(uploaded_file)
        else:
            st.warning("기본 파일이 없고, 업로드된 파일도 없습니다.")
            return None

# 데이터 불러오기
df = load_data()

if df is not None:
    # MBTI 유형 선택
    mbti_types = [col for col in df.columns if col != "Country"]
    selected_type = st.selectbox("MBTI 유형을 선택하세요", mbti_types)
    
    # 상위 10개 국가 추출
    top10 = df[["Country", selected_type]].sort_values(by=selected_type, ascending=False).head(10)
    
    st.subheader(f"📊 {selected_type} 유형 비율 상위 10개국")
    st.dataframe(top10, use_container_width=True)
    
    # Altair 차트
    chart = (
        alt.Chart(top10)
        .mark_bar()
        .encode(
            x=alt.X(selected_type, title="비율"),
            y=alt.Y("Country", sort="-x", title="국가"),
            tooltip=["Country", selected_type]
        )
        .properties(width=700, height=400)
    )
    
    st.altair_chart(chart, use_container_width=True)
