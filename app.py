import flask from flask
import streamlit as st
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
if __name__ == '__main__':
    app.run(debug=True)

st.title("Moja pierwsza aplikacja Streamlit")
st.write("Witaj w mojej aplikacji Streamlit!")

name = st.text_input("Podaj swoje imię")
st.write(f"Cześć, {name}!")
