import streamlit as st
from gigachat_api import send_prompt, get_access_token, sent_prompt_and_get_response

st.title("AbionaBot")

if "access_token" not in st.session_state:
    try:
        st.session_state.access_token = get_access_token()
        st.toast(f"Токен доступа получен успешно!")
    except Exception as e:
        st.toast(f"Ошибка при получении токена доступа!")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "ai", "content": "Привет! Я AbionaBot. Чем могу быть полезен?"}
    ]

for msg in st.session_state.messages:
    if msg.get("is_image"):
        st.chat_message(msg["role"]).image(msg["content"])
    else:
        st.chat_message(msg["role"]).write(msg["content"])

if user_promt := st.chat_input():
    st.chat_message("user").write(user_promt)
    st.session_state.messages.append({"role": "user", "content": user_promt})

    with st.spinner("В процессе..."):
        response, is_image = sent_prompt_and_get_response(
            user_promt, st.session_state.access_token
        )
        if is_image:
            st.chat_message("ai").image(response)
            st.session_state.messages.append(
                {"role": "ai", "content": response, "is_image": True}
            )
        else:
            st.chat_message("ai").write(response)
            st.session_state.messages.append({"role": "ai", "content": response})
