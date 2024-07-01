import streamlit as st

st.title("Moja pierwsza aplikacja Streamlit")
st.write("Witaj w mojej aplikacji Streamlit!")

bg_color = st.color_picker("Wybierz kolor tła", "#FFFFFF")

if st.button("Zatwierdź kolor tła"):
    st.session_state.bg_color = bg_color

if 'bg_color' in st.session_state:
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {st.session_state.bg_color};
        }}
        </style>
        """, unsafe_allow_html=True)

if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter():
    st.session_state.count += 1

st.button("Kliknij mnie!", on_click=increment_counter)
st.write(f"Liczba kliknięć: {st.session_state.count}")
