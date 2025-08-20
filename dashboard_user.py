import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib import font_manager, rcParams
from pathlib import Path

@st.cache_resource
def setup_korean_font():
    font_dir = Path(__file__).parent
    # 원하는 폰트 파일명으로 교체 가능
    font_paths = [font_dir / "Pretendard.ttf"]
    print(font_paths)
    for p in font_paths:
        if p.exists():
            font_manager.fontManager.addfont(str(p))
            
    plt.rcParams['font.family'] = 'Pretendard'  # 한글 폰트 설정
    plt.rcParams['axes.unicode_minus'] = False   # 마이너스 기호 표시 설정
    plt.rcParams['font.size'] = 10

setup_korean_font()

def create_visitor_chart():
    # 임의의 방문자 수 데이터 생성 (7일치)
    np.random.seed(np.random.randint(0, 100))
    dates = pd.date_range(end=datetime.now(), periods=7).strftime("%m/%d").tolist()
    visitors = np.random.randint(1, 30, size=7)
    return visitors

class DashboardUser:
    def __init__(self):
        self.title = "User Dashboard"
    
    def visit_user(select_day):
        st.write("사용자 방문수")
        dates = [select_day - timedelta(days=i) for i in range(6, -1, -1)]
        date_labels = [d.strftime('%m/%d') for d in dates]
        np.random.seed(select_day.day)                        # 랜덤 시드 설정
        total_visitors = np.random.randint(20, 50, size=7)    # 전체 방문자 수
        
        df = pd.DataFrame({
            '날짜': date_labels,
            '전체 방문자 수': total_visitors
        })
        st.line_chart(df, x='날짜', y='전체 방문자 수')
    
    def visit_new_user(select_day):
        st.write("새 사용자 방문수")
        dates = [select_day - timedelta(days=i) for i in range(6, -1, -1)]
        date_labels = [d.strftime('%m/%d') for d in dates]
        np.random.seed(select_day.day)                        # 랜덤 시드 설정
        total_visitors = np.random.randint(20, 50, size=7)    # 전체 방문자 수
        
        df = pd.DataFrame({
            '날짜': date_labels,
            '새 방문자 수': total_visitors
        })
        
        st.line_chart(df, x='날짜', y='새 방문자 수')
    
    def show_user():
        st.write("사용자 현황")
        labels = 'Institution', 'General'
        sizes  = [362, 289]
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', 
                radius=1.0, startangle=90)
        ax.margins(x=0, y=0)    # 여백지우기
        st.pyplot(fig)

    def institution_user():
        st.write("기관별 가입자 수")
        fig, ax = plt.subplots(figsize=(5, 4.5))
        institutions = ['Koroad', 'KATECH','DIP','Mobigen', 'Datacook']
        counts = [177, 29, 22, 16, 4]
        bar_labels = ['Koroad', 'KATECH','DIP','Mobigen', 'Datacook']
        bar_colors = ['tab:green', 'tab:blue', 'tab:red', 'tab:cyan', 'tab:orange']
        ax.bar(institutions, counts, label=bar_labels, color=bar_colors)
        ax.set_ylabel('기관별 가입자 수')
        st.pyplot(fig)

    def usage_mydisk(today):
        np.random.seed(today.day)
        st.write("MyDisk 사용 현황")
        fig, ax = plt.subplots(figsize=(5, 4.5))
        people = []
        usage  = []
        for i in range(5):
            num = np.random.randint(300)
            use = np.random.randint(500)
            people.append(f"user_{num}")
            usage.append(use)

        y_pos = np.arange(len(people))
        ax.barh(y_pos, usage, align='center', alpha=0.5,
                color='blue')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(people)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('사용량 (GB)')
        st.pyplot(fig)  

    def occurrence_event(select_day):
        col_1, col_2 = st.columns(2)
        with col_1:
            st.write("이벤트 발생 현황")            
        with col_2:
            evnet = st.selectbox(
                "Select an event",
                ("page_view", "click"),
                index=0,
                label_visibility="collapsed"    
            )
        if evnet == "page_view":
            dates = [select_day - timedelta(days=i) for i in range(6, -1, -1)]
            date_labels = [d.strftime('%m/%d') for d in dates]
            np.random.seed(select_day.day)                   
            page_views = np.random.randint(100, 500, size=7)    # 전체 방문자 수
            
            df = pd.DataFrame({
                'date': date_labels,
                'page_views': page_views
            })
            st.line_chart(df, y='page_views')
        elif evnet == "click":
            dates = [datetime.today() - timedelta(days=i) for i in range(6, -1, -1)]
            date_labels = [d.strftime('%m/%d') for d in dates]
            np.random.seed(select_day.day-1)                   
            clicks = np.random.randint(100, 500, size=7)        # 전체 방문자 수
            
            df = pd.DataFrame({
                'date': date_labels,
                'clicks': clicks
            })
            st.line_chart(df, y='clicks')
