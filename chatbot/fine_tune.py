# fine_tune.py
from openai import OpenAI
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 학습 데이터 파일 업로드
file = client.files.create(
    file=open("training_data.jsonl", "rb"),  # 학습 데이터 파일
    purpose="fine-tune"
)

# 파인튜닝 작업 생성
job = client.fine_tuning.jobs.create(
    training_file=file.id,  # 업로드된 파일 ID
    model="gpt-3.5-turbo",  # 파인튜닝할 모델
    suffix="incheon-uni-bot"  # 모델 이름 접미사
)

print(f"파인튜닝 작업 ID: {job.id}")
print(f"모델이 완료되면 다음 ID를 사용하세요: ft:gpt-3.5-turbo:your-org-name::{job.id}")