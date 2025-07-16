import streamlit as st

# 책 정보: 제목 + 이미지 URL
mbti_books = {
    "INTJ": [
        ("도덕경 - 노자", "https://upload.wikimedia.org/wikipedia/commons/9/9e/Tao_Te_Ching_%28Chinese%29.jpg"),
        ("군주론 - 마키아벨리", "https://upload.wikimedia.org/wikipedia/commons/8/8c/Il_Principe_%281532%29.png"),
        ("월든 - 헨리 데이비드 소로", "https://upload.wikimedia.org/wikipedia/commons/8/88/Walden_Thoreau.jpg")
    ],
    "INFP": [
        ("어린 왕자 - 생텍쥐페리", "https://upload.wikimedia.org/wikipedia/commons/8/88/Littleprince.JPG"),
        ("폭풍의 언덕 - 에밀리 브론테", "https://upload.wikimedia.org/wikipedia/commons/5/5d/Wuthering_Heights_%281st_ed%29.jpg"),
        ("빨간 머리 앤 - 루시 모드 몽고메리", "https://upload.wikimedia.org/wikipedia/commons/1/1e/Anne_of_Green_Gables_%281908%29_cover.jpg")
    ],
    "ENTP": [
        ("갈릴레오의 생애 - 브레히트", "https://upload.wikimedia.org/wikipedia/commons/b/bb/Bertolt_Brecht_Galileo.jpg"),
        ("이방인 - 알베르 카뮈", "https://upload.wikimedia.org/wikipedia/commons/f/f1/L%27%C3%A9tranger_%28Camus_novel%29.jpg"),
        ("변신 - 카프카", "https://upload.wikimedia.org/wikipedia/commons/2/29/Metamorphosis_by_Franz_Kafka_first_edition.jpg")
    ]
    # 필요한 만큼 MBTI 추가 가능
}

def main():
    st.title("📚 MBTI별 고전책 추천")
    st.subheader("당신의 MBTI에 어울리는 고전을 골라드릴게요!")

    mbti_list = sorted(mbti_books.keys())
    selected_mbti = st.selectbox("당신의 MBTI는?", mbti_list)

    if selected_mbti:
        st.markdown("### 💡 추천 도서")
        for title, img_url in mbti_books[selected_mbti]:
            st.markdown(f"**{title}**")
            st.image(img_url, width=150)
            st.markdown("---")

    st.caption("© 2025 BookMatch | MBTI별 고전 큐레이션")

if __name__ == "__main__":
    main()
