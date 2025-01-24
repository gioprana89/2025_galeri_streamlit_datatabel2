import streamlit as st 

st.set_page_config(layout="wide")

import pandas as pd

import numpy as np

import plotly.graph_objects as go

import plotly.express as px







st.write('''<br><br><br><center><font color = "#0000ff" size = 7>APLIKASI PYTHON-STREAMLIT: DATA TABEL-2</font></center>



             ''', unsafe_allow_html = True)



st.write('''<br><left><font color = "#ff3814" size = 3>Aplikasi berikut menampilkan data tabel yang diimport dari data excel. Data yang disajikan membuat link, yang apabila di-click, akan menuju ke suatu alamat website</font><font color = "blue" style="background-color: #d0ff14"><a href = "https://github.com/gioprana89/2025_galeri_streamlit_datatabel2" target = '_blank' style = 'text-decoration:none'> Download Kode.</a></font>



             ''', unsafe_allow_html = True)




dataku = pd.read_excel("data excel.xlsx")



dataku = pd.DataFrame(dataku)




st.data_editor(
    dataku,
    column_config={

        "Link": st.column_config.LinkColumn(
            "Link Website", display_text="Alamat Website"
        ),
    },
    hide_index=True,
)

