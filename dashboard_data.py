import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

plt.rcParams['font.family'] = 'NanumGothic'  # 한글 폰트 설정
plt.rcParams['axes.unicode_minus'] = False   # 마이너스 기호 표시 설정
plt.rcParams['font.size'] = 10

# @staticmethod
def create_data(today, part):
    months  = []
    totals  = []
    datas   = []
    np.random.seed(today.month)
    for i in range(6, 0, -1):
        month = f"{today.month-i}월"
        if part == '국내':
            total = np.random.randint(1000, 2000)
            data  = np.random.randint(300, 1000)
        else:
            total = np.random.randint(1500, 3000)
            data  = np.random.randint(500, 1500)
        months.append(month)
        totals.append(total)
        datas.append(data)

    return months, totals, datas

class DashboardData:
    @staticmethod
    def show_data_overview():
        st.write("데이터 유형별 수집량(GB)")
        con = st.container(border=True, height=125)
        with con:
            st.metric("Total", "5210GB", "+10%")
        
        col_2, col_3, col_4 = st.columns(3, gap="small")
        with col_2:
            con_2 = st.container(border=True, height=130,)
            with con_2:
                st.metric(label="Image", value="1400GB", delta="-10%")            
        with col_3:
            con_3 = st.container(border=True, height=130)
            with con_3:
                st.metric("CSV", "1510GB", "+15%")            
        with col_4:
            con_4 = st.container(border=True, height=130)
            with con_4:
                st.metric("etc.", "2300GB", "+2%")            

    def show_related_data(today):
        col_1, col_2 = st.columns([8,2])
        col_1.write("연계 데이터 현황(수집량, 자동차 산업 데이터 수)")
        with col_2:
            tag = st.pills("국내/해외", 
                           ["국내", "해외"], 
                           selection_mode="single", 
                           default="국내",
                           label_visibility="collapsed")
        
        fig, ax = plt.subplots(figsize=(10, 3.5))   # figsize = (x축, y축)
        if tag == "국내":
            months, totals, datas = create_data(today, tag)
        else:
            months, totals, datas = create_data(today, tag)

        counts = {
            "total": np.array(totals),
            "data" : np.array(datas),
        }
        width = 0.5
        bottom = np.zeros(len(months))        
        for boolean, count in counts.items():
            p = ax.bar(months, count, width, label=boolean)
            bottom += count

        ax.legend(loc="upper left")
        st.pyplot(fig)
    
    def data_collection_status():
        col_1, col_2 = st.columns([2,1])
        col_1.write("산업 카테고리 별 데이터 수집 현황")
        with col_2:
            tag_2 = st.pills("국내/해외", 
                             ["국내", "해외"], 
                             selection_mode="single", default="국내", 
                             key="category",
                             label_visibility="collapsed")

        if tag_2 == "국내":
            fig, ax = plt.subplots()
            categories = ["부품제조", "자동차제조", "판매/정비", "이용", "관제", "미래차", "기타"]
            counts = [5104, 416, 2648, 11, 2344, 258, 1332]
            ax.set_position([0, 0, 1, 1])  # 축을 전체 영역으로 확장
            ax.pie(counts, labels=categories, startangle=140, frame=False, radius=1.0, center=(0,1))
            ax.legend(loc="best", bbox_to_anchor=(1, 1.0), fontsize=8)
        else:
            fig, ax = plt.subplots(figsize=(8, 5))
            categories = ["부품제조", "자동차제조", "판매/정비", "이용", "관제", "미래차", "기타"]
            counts = [2635, 13, 13182, 80, 3667, 3370, 1230]    
            ax.set_position([0, 0, 1, 1])  # 축을 전체 영역으로 확장
            ax.pie(counts, labels=categories, startangle=110, frame=False, radius=1.0, center=(0,1))
            ax.legend(loc="best", bbox_to_anchor=(1, 1.0), fontsize=8)

        plt.tight_layout()
        st.pyplot(fig, clear_figure=True, use_container_width=True)
        
    def data_Utilization_Status(today):
        np.random.seed(today.day)  # 랜덤 시드 설정
        start_day = today - timedelta(days=7)
        df = pd.DataFrame(np.random.randint(100, 500, size=(7, 3)),
                          index=pd.date_range(start=start_day, periods=7, freq='D'),
                          columns=['공유', '조회','다운로드'])
        
        st.line_chart(df, use_container_width=True, x_label='닐찌', y_label='활용 수')

    
    def top10_Data_Views():
        st.write("조회수 Top10 데이터")
