from openai import OpenAI
import time
import streamlit as st

# 코드스니펫 - 제목
st.title('제품 홍보 자동 생성기')

# 코드스니펫 - 입력
text1 = st.text_input("입력해보세요")

# 코드스니펫 - 버튼

if st.button('노크하기'):
  st.write('여기 사람 있어요')

# 코드스니펫 - 제목
st.title('[스파르타] 제품 홍보 포스터 생성기')

# 코드스니펫 - 입력
keyword = st.text_input("키워드를 입력하세요.")

# 코드스니펫 - 버튼
if st.button('생성 :fire:'):
  st.write('여기에 API 붙여넣기')
  # 코드스니펫 - 스피너

  with st.spinner('Wait for it...'):

    client = OpenAI(api_key=st.secrets["API_KEY"])

    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": keyword + '라는 주제의 홍보포스터 카피를 50자 이내로 만들어줘',
        }],
        model="gpt-4o",
    )

    chat_result = chat_completion.choices[0].message.content
    st.write(chat_result)

    client = OpenAI(api_key=st.secrets["API_KEY"])

    response = client.images.generate(
        model="dall-e-3",
        prompt=keyword,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
# 코드스니펫 - 이미지
st.image(image_url)
