import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 読み込み
load_dotenv()

# APIキー取得
api_key = os.getenv("OPENAI_API_KEY")

# OpenAIクライアント作成
client = OpenAI(api_key=api_key)

# prompt.txt読み込み
with open("prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

# タイトル
st.title("VYRE")
st.subheader("Health × Bodymake AI")

# 食品入力
food = st.text_input("食べたものを入力してください")

# 評価ボタン
if st.button("評価する"):

    if food:

        with st.spinner("AIが分析中..."):

            # GPTへ送信
            response = client.chat.completions.create(

                model="gpt-4.1-mini",

                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": food
                    }
                ],

                temperature=0.7
            )

            # 結果取得
            result = response.choices[0].message.content

        # 結果表示
        st.write("## 評価結果")
        st.write(result)

    else:
        st.warning("食品名を入力してください")