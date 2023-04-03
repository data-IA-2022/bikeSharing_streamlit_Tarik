from st_on_hover_tabs import on_hover_tabs
import streamlit as st
st.set_page_config(page_title='Bike Sharing App', page_icon = "https://account.capitalbikeshare.com/favicon.ico", layout="wide", initial_sidebar_state = "auto")


st.header("Custom tab component for on-hover navigation bar")

st.markdown('<style>' + open('./static/css/style.css').read() + '</style>', unsafe_allow_html=True)
st.markdown('<img src="https://cdn.lyft.com/static/bikesharefe/logo/CapitalBikeshare-main.svg" alt="Capital Bikeshare" class="sc-gXmSlM dXSSil">', unsafe_allow_html=True)


with st.sidebar:
    with st.sidebar:
        st.markdown('<img src="./static/assets/images/cpbikeshare-logo.png" alt="Capital Bikeshare" class="bshare-logo">', unsafe_allow_html=True)
        tabs = on_hover_tabs(tabName=['Home', 'Money', 'Economy'], 
                             iconName=['home', 'money', 'economy'],
                             styles = {'navtab': {'background-color':'#fff',
                                                  'color': '#818181',
                                                  'font-size': '18px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                       'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                      'cursor': 'pointer'}},
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'}},
                             key="1")

if tabs =='Dashboard':
    st.title("Navigation Bar")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Money':
    st.title("Paper")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Economy':
    st.title("Tom")
    st.write('Name of option is {}'.format(tabs))