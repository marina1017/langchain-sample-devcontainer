import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    # システムメッセージ
    SystemMessage, 
    # 人間の質問
    HumanMessage, 
    # ChatGPTの返答
    AIMessage)
from langchain.callbacks import get_openai_callback
from langchain.callbacks import StreamlitCallbackHandler


# 環境変数を使用する
from dotenv import load_dotenv
import os

def init_page():
    # .envファイルを読み込む
    load_dotenv()

    ## streamlitの設定 
    st.set_page_config(
        page_title="My Great ChatGPT",
        page_icon="🤗"
    )
    st.header("My Great ChatGPT 🤗")

    # サイドバーのタイトルを表示
    st.sidebar.title("Options")
    

def select_model():
    # サイドバーにオプションボタンを設置
    model = st.sidebar.radio("Choose a model:",("GPT-3.5", "GPT-4"))
    if model == "GPT-3.5":
        model_name = "gpt-3.5-turbo"
    else:
        model_name = "gpt-4"
    # サイドバーにスライダーを追加し、temperatureを0から2までの範囲で選択可能にする
    # 初期値は0.0、刻み幅は0.1とする
    temperature = st.sidebar.slider("Temperature:", min_value=0.0, max_value=2.0, value=0.0,step=0.01)
        
    # ChatGPT APIを呼んでくれる機能
    return ChatOpenAI(temperature=temperature, openai_api_key=os.environ.get("OPENAI_API_KEY"), model_name=model_name)

def init_messages():
    # サイドバーにボタンを設置
    clear_button = st.sidebar.button("Clear Conversation", key="clear")
    if clear_button or "message" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]
        st.session_state.cost = []
        st.session_state.token = []

def get_answer(llm, messages):
    with get_openai_callback() as cb:
        answer = llm(messages) 
    return answer.content, cb.total_cost, cb.total_tokens

def main():
    init_page()
    llm = select_model()
    init_messages()

    # チャット履歴の初期化
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]

    # ユーザーの入力を監視
    if user_input := st.chat_input("聞きたいことを入力してね！"):
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("ChatGPT is typing ..."):
            answer, cost, token = get_answer(llm,st.session_state.messages)
        st.session_state.cost.append(cost)
        st.session_state.token.append(token)
        st.session_state.messages.append(AIMessage(content=answer))
        
    # # チャット履歴の表示
    messages = st.session_state.get('messages', [])
    for message in messages:
        if isinstance(message, AIMessage):
            with st.chat_message('assistant'):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message('user'):
                st.markdown(message.content)
        else:  # isinstance(message, SystemMessage):
            st.write(f"System message: {message.content}")

    # コスト表示
    costs = st.session_state.get('cost', [])
    st.sidebar.markdown("## costs")
    st.sidebar.markdown(f"### totalcosts: ${sum(costs):.5f}")
    for cost in costs:
        st.sidebar.markdown(f"- ${cost:.5f}")

    # トークン表示
    tokens = st.session_state.get('token', [])
    st.sidebar.markdown("## tokens")
    st.sidebar.markdown(f"### totaltokens: {sum(tokens):.5f}")
    for token in tokens:
        st.sidebar.markdown(f"- {token:.5f}")

if __name__ == '__main__':
    main()