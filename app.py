import streamlit as st

# タイトルの設定
st.title("Hello Streamlit!")

# サイドバーにウィジェットを追加
st.sidebar.header("設定")
name = st.sidebar.text_input("あなたの名前を入力してください")

# メインエリア
st.write("## Welcome to my Streamlit App!")

if name:
    st.write(f"こんにちは、{name}さん！")
    st.balloons()

# データ表示の例
import pandas as pd
import numpy as np

# サンプルデータの作成
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.write("### サンプルデータ")
st.line_chart(chart_data)

# ボタンの例
if st.button("クリックしてください"):
    st.success("ボタンがクリックされました！")
