# import Libraries
import  streamlit as st
import eda
import prediction
from streamlit_option_menu import option_menu

# section navigasi
with st.sidebar:
  navigation = option_menu(
    menu_title = "Main Menu",
    options = ["EDA","Predictor"],
    icons = ["bar-chart-fill","easel-fill"],
    menu_icon =  'menu-down',
    default_index = 0
  )

# halaman
if navigation == 'Predictor':
    prediction.run()
elif navigation == 'EDA':
    eda.run()