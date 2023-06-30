import streamlit as st
import pandas as pd


# 读取CSV文件
df = pd.read_csv("ai_model_test.csv", index_col="id")

# 获取ID列表
id_list = df.index.tolist()

# Streamlit应用
def main():
    st.title("展示文本和图片")

    # 用户选择ID
    selected_id = st.sidebar.selectbox("选择ID", id_list)

    # 获取所选ID对应的行
    selected_row = df.loc[selected_id]

    # 获取文本字段
    selected_text = selected_row["prompt"]
    st.markdown(f"**文本**:\n{selected_text}")

    # 获取图片链接字段
    image_urls = selected_row.drop("prompt").values.tolist()

    # 展示图片
    for i, url in enumerate(image_urls):
        column_name = selected_row.index[i + 1]
        st.markdown(f"**{column_name}**:")
        st.image(url, use_column_width=True)


if __name__ == "__main__":
    main()