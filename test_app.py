# test app

import streamlit as st

st.set_page_config(
        page_title="Test app", page_icon=":chart_with_upwards_trend:",
        layout='wide'
    )

def main():
    st.title("Test")

if __name__ == "__main__":

    main()