# 자동차데이터플랫폼 사용현황 대시보드

본 프로젝트는 **자동차데이터플랫폼(Korea Automotive Data Platform)** 의 서비스 및 자원 사용 현황을 모니터링하기 위한 **Streamlit 기반 대시보드**입니다.  
사용자, 데이터, GPUaaS 세 가지 영역으로 나누어 시각화를 제공하며, 플랫폼의 활용도를 직관적으로 확인할 수 있도록 개발되었습니다.

🚀 [대시보드 바로가기](https://kadap-dashboard.streamlit.app/)

---

## 📌 주요 기능

### 👥 사용자(User) 대시보드
- 사용자 방문 수 추이 (전체 / 신규 사용자)
- 사용자 유형별 비율 (기관 사용자 vs 일반 사용자)
- 기관별 가입자 수 통계
- MyDisk 저장소 사용 현황
- 이벤트 발생 현황 (page view, click 등)

### 📂 데이터(Data) 대시보드
- 데이터 유형별 수집량(GB) 및 변화 추이
- 국내/해외 연계 데이터 현황
- 산업 카테고리별 데이터 수집 현황 (부품제조, 자동차제조, 판매/정비, 미래차 등)
- 데이터 활용 현황 (공유, 조회, 다운로드)
- 조회수 Top10 데이터

### 🖥️ GPUaaS 대시보드
- GPU 사용률 (NVIDIA A40, H100)
- 워크로드 현황 (실행중, 대기중, 에러 상태)
- 기관별 GPU 사용시간 (제타모빌리티, 모비젠, 서울대, 데이터쿡 등)
- 노드별 사용량 조회 (master/worker 노드)

---

## 📂 프로젝트 구조
```plaintext
kadap_dashboard/
├── dashboard_v2.py        # 메인 실행 파일 (Streamlit 앱 시작 지점)
├── dashboard_user.py      # 사용자(User) 관련 시각화 모듈
├── dashboard_data.py      # 데이터(Data) 관련 시각화 모듈
├── dashboard_gpu.py       # GPUaaS(GPU 사용현황) 관련 시각화 모듈
├── asset/                 # 리소스 (이미지, 폰트 등)
│   ├── fonts/             # Pretendard.ttf 등 한글 폰트
│   └── images/            # 아이콘 및 시각화용 이미지
├── requirements.txt       # 의존성 패키지 목록
└── README.md              # 프로젝트 설명 문서
```

## ⚙️설치 및 실행 방법
### 1. 저장소 클론
```bash
git clone https://github.com/MINJU-B/kadap_dashboard.git
cd kadap_dashboard
```

### 2. 가상환경 생성 및 활성화
```
# 가상환경 생성
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. 패키지 설치
```
pip install -r requirements.txt
```

### 4. Streamlit 실행
```
streamlit run dashboard_v2.py
```

### 5. 브라우저 접속
실행 후 터미널에 표시된 주소(http://localhost:8501)로 접속하면 대시보드를 확인할 수 있습니다.
