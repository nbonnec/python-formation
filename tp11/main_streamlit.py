#!/usr/bin/env python

import streamlit as st

from UserDAO import UserDAO


def main():
    st.set_page_config(layout="wide")
    st.write('Hello world!')
    title = st.text_input('Movie title', 'Life of Brian')
    if st.button('Show movie') and title:
        st.write('The current movie title is', title)

    dao = UserDAO('deb.db')
    users = dao.find_all()
    st.table(users)


if __name__ == '__main__':
    main()
