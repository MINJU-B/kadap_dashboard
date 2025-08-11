import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

plt.rcParams['font.family'] = 'NanumGothic'  # 한글 폰트 설정
plt.rcParams['axes.unicode_minus'] = False   # 마이너스 기호 표시 설정
plt.rcParams['font.size'] = 10

class DashboardGPU():
    @staticmethod
    def usage_A40(today):
        np.random.seed(today.day)           # 랜덤 시드 설정
        st.write('NVIDIA A40 사용률')        
        fig, ax = plt.subplots(figsize=(8,3)) 
        working = np.random.randint(70)
        ratio  = [working,100-working]
        labels = ['가동중', '비가동']
        colors = ['#5faff5' ,'#c1c2c1']
        wedgeprops={'width': 0.6, 'edgecolor': 'w', 'linewidth': 5}
        ax.pie(ratio, labels=labels, autopct='%.1f%%', startangle=90, radius=0.8, counterclock=False, colors=colors, wedgeprops=wedgeprops)
        plt.tight_layout()
        st.pyplot(fig)

    def usage_H100():
        st.write('NVIDIA H100 사용률')        
        fig, ax = plt.subplots(figsize=(8,3))
        working = np.random.randint(70)
        ratio  = [working,100-working]
        labels = ['가동중', '비가동']
        colors = ['#f35b39' ,'#c1c2c1']
        wedgeprops={'width': 0.6, 'linewidth': 5}
        ax.pie(ratio, labels=labels, autopct='%.1f%%', startangle=90, radius=0.8, counterclock=False, colors=colors, wedgeprops=wedgeprops)
        plt.tight_layout()
        st.pyplot(fig)

    def state_workload(today):
        st.write('워크로드 사용 현황')        
        col_1, col_2 = st.columns([1,1])
        np.random.seed(today.day)
        working = np.random.randint(0,5)
        waiting = np.random.randint(0,working)
        error   = np.random.randint(0,1)
        if working + waiting + error > 5:
            working = 5
            waiting = 0
            error   = 0
        else:
            working = 5-(waiting + error)
            
        with col_1:
            st.image('./image/all_5110777.png', width=50)
            st.subheader('전체')
            st.subheader(working+waiting+error)
        with col_2:
            st.image('./image/refresh_16876526.png', width=50)
            st.subheader('실행중')
            st.subheader(working)
        
        col_3, col_4 = st.columns([1,1])
        with col_3:
            st.image('./image/stop_142458.png', width=50)
            st.subheader('대기중')
            st.subheader(waiting)
        with col_4:
            st.image('./image/error_1008930.png', width=50)
            st.subheader('에러')
            st.subheader(error)

    def usetime_gpu(today):
        st.write('기관별 GPU 사용시간') 
        organization = ['제타모빌리티', '모비젠', '서울대학교', '데이터쿡']
        np.random.seed(today.day)
        v100_uses = [np.random.randint(10, 200) for _ in organization]
        A40_uses  = [np.random.randint(10, 200) for _ in organization]
        H100_uses = [np.random.randint(10, 200) for _ in organization]

        # 막대그래프 y위치 설정
        y = np.arange(len(organization))
        bar_height = 0.15

        # Figure 생성
        fig, ax = plt.subplots(figsize=(12, 2.9))

        # GPU별 수평 막대 추가
        ax.barh(y - bar_height, v100_uses, height=bar_height, label='V100', color='skyblue')
        ax.barh(y,               A40_uses, height=bar_height, label='A40',  color='lightgreen')
        ax.barh(y + bar_height, H100_uses, height=bar_height, label='H100', color='salmon')        

        # y축 라벨 및 기타 설정
        ax.set_yticks(y)
        ax.set_yticklabels(organization)
        ax.set_xlabel('사용 시간 (시간)')
        # ax.set_title('기관별 GPU 사용 시간')
        ax.legend()

        plt.tight_layout()
        st.pyplot(fig)

    def usage_nodes():
        col_1, col_2 = st.columns(2)

        with col_1:
            st.write('노드별 사용량')        
        with col_2:            
            node = st.selectbox('nodes', 
                            ['master_01', 'master_02', 'master_03', 'worker_gpu01', 'worker_gpu02', 'worker_gpu02'], 
                            label_visibility='collapsed')

        if node == 'master_01':
            st.write("matser_01의 사용량")
        if node == 'master_02':
            st.write("matser_02의 사용량")