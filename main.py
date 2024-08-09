import streamlit as st
import os

st.set_page_config(layout="wide")

st.title(":writing_hand: :robot_face: :thumbsup: ChatBot :kr:")

col1, col2 = st.columns([1,4])

col1.markdown("만든이")
col1.markdown(":man: [Taehee](https:researchgate.net/profile/Taehee-Lee)")
col1.markdown(":email: [이메일 보내기](mailto:thlee420@gmail.com)")

col2.markdown(
        """
    OpenAI API 키 발급 방법은 아래 링크를 참고해 주세요!
    * [발급방법](https://wikidocs.net/233342)
    """
    )


# API 키 입력
api_key = col2.text_input("API 키 입력", type="password")

    # 설정 확인 버튼
confirm_btn = col2.button("설정하기", key="api_key")

if confirm_btn:
    os.environ["OPENAI_API_KEY"] = api_key
    col2.write(f"API 키가 설정되었습니다: `{api_key[:15]}************`")

