import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.image("https://static.independent.co.uk/s3fs-public/thumbnails/image/2018/02/19/11/ali-baba-kebab.jpg?width=1200", caption="чай делим пополам", width=500)

st.write("""
# YO BRATISHQUA
# Давай посмотрим, что у нас там с чаем
""")

st.write("""
**<- Загрузи файл слева, иначе право не получится**
""")



uploaded_file = st.sidebar.file_uploader("Загрузи CSV файл", type="csv")


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Распределение чаевых")
    fig, ax = plt.subplots()
    sns.histplot(df["tip"], kde=True, ax=ax)
    st.pyplot(fig)

    with open("tips_for_my_peeps.png", "wb") as f:
        plt.savefig(f)
    st.download_button("Скачать график", open("tips_for_my_peeps.png", "rb"))
    st.write("""
    # **У НАС ВСЕ ПОЛУЧИЛОСЬ, УРА!**
    """)
    st.image("https://media.tenor.com/FR3k-v4wJ4YAAAAM/kebab-jumpscare.gif", width=500)
