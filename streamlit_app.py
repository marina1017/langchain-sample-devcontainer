import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)


def main():
    st.set_page_config(
        page_title="My Great ChatGPT",
        page_icon="🤗"
    )
    st.header("My Great ChatGPT 🤗")
    # input
    if user_input := st.chat_input("聞きたいことを入力してね！"):
        print("hoge")
    
    # input
    container = st.container()
    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_area(label="ききたいことを入力してね:",key="input",height=100)
            submit_button = st.form_submit_button(label="Send")
        if submit_button and user_input:
            # なにか入力されればここが実行される
            print("hogehogehgoe")

if __name__ == '__main__':
    main()