from openai import OpenAI
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

job_id = "ftjob-uaURunPrvT08CQrdizbwSqYw"  # 실제 작업 ID 입력

# 작업 정보 및 이벤트 가져오기
job_info = client.fine_tuning.jobs.retrieve(job_id)
events = client.fine_tuning.jobs.list_events(job_id)

# 이벤트 출력
for event in events:
    print(event.created_at, event.level, event.message)  # 속성 접근 방식으로 수정
print("현재 작업 상태:", job_info.status)
print("파인튜닝된 모델 이름:", job_info.fine_tuned_model)
