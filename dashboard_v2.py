import streamlit as st
#import altair as alt
from datetime import datetime
from dashboard_user import DashboardUser
from dashboard_data import DashboardData
from dashboard_gpu  import DashboardGPU

st.set_page_config(
    page_title = "자동차데이터플랫폼 Dashboard",
    layout     = "wide",
    initial_sidebar_state = "expanded"
)
#alt.themes.enable("dark")

with st.sidebar:
    # Select Menu
    add_selectmenu = st.sidebar.selectbox(
        "Choose your dashboard MENU",
        ("USER", "DATA", "GPUaaS"),
        index=2 
    )  

    # Select Date
    select_day = st.sidebar.date_input(
        "Select a date",
        datetime.today()    
    )

if add_selectmenu == "USER":
    # call dashboard_user.py
    col_1, col_2, col_3 = st.columns(3)
    col_4, col_5, col_6 = st.columns(3)

    with col_1:
        with st.container(border=True, height=400):
            DashboardUser.visit_user(select_day)
    with col_2:
        with st.container(border=True, height=400):
            DashboardUser.visit_new_user(select_day)
    with col_3:
        with st.container(border=True, height=400):
            DashboardUser.show_user()

    with col_4:
        with st.container(border=True, height=400):
            DashboardUser.institution_user()

    with col_5:
        with st.container(border=True, height=400):
            DashboardUser.usage_mydisk(select_day)

    with col_6:
        with st.container(border=True, height=400):
            DashboardUser.occurrence_event(select_day)

elif add_selectmenu == "DATA":
    # call dashboard_data.py           
    col_1, col_2 = st.columns([1,2])
    
    with col_1:
        with st.container(border=True, height=420):
            # DashboardData.show_data_overview()
            DashboardData.data_collection_status()
    with col_2:
        with st.container(border=True, height=420):
            DashboardData.show_related_data(select_day)
    
    col_3, col_4 = st.columns([1.5,1.5])
    with col_3:
        with st.container(border=True, height=360):
            # DashboardData.data_collection_status()
            DashboardData.show_data_overview()
    with col_4:
        with st.container(border=True, height=360):
            tag = st.selectbox(
                " ",
                ["데이터 활용 현황",
                 "조회수 Top10 데이터"],
                 label_visibility="collapsed",
                index=0
            )
            if tag == "데이터 활용 현황":
                DashboardData.data_Utilization_Status(select_day)
            elif tag == "조회수 Top10 데이터":
                DashboardData.top10_Data_Views()
    
else:
    # call dashboard_gpu.py
    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        with st.container(border=True, height=400):
            DashboardGPU.usage_A40(select_day)
    with col_2:
        with st.container(border=True, height=400):
            DashboardGPU.usage_H100()
    with col_3:
        with st.container(border=True, height=400):
            DashboardGPU.state_workload(select_day)

    # col_4, col_5 = st.columns([2,1])
    # col_4 = st.columns(1)
    # with col_4:
    with st.container(border=True, height=380):
        DashboardGPU.usetime_gpu(select_day)
    # with col_5:
    #     with st.container(border=True, height=380):       
    #         DashboardGPU.usage_nodes()
    


