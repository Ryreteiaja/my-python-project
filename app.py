import streamlit as st
import pandas as pd

st.title("Filter App")

# CSVアップロード
uploaded_file = st.file_uploader("CSVファイルを選択してください", type="csv")

if uploaded_file is not None:

    # CSV読み込み
    df = pd.read_csv(uploaded_file)

    st.write("### 元データ")
    st.dataframe(df)

    st.write("### フィルター設定")

    # 数値列取得
    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    # フィルター列選択
    filter_column = st.selectbox("フィルター列を選択", numeric_columns)

    # 最小値入力
    min_value = st.slider(
        "最小値を選択",
        int(df[filter_column].min()),
        int(df[filter_column].max()),
        int(df[filter_column].min())
    )

    # フィルター
    filtered_df = df[df[filter_column] >= min_value]

    st.write("### フィルター後データ")
    st.dataframe(filtered_df)

    # グラフ表示
    st.write("### グラフ")


    st.line_chart(df["sales"]) #折れ線グラフ表示