from openai import OpenAI
import os
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS

# 환경 변수 로드
load_dotenv()

# Flask 애플리케이션 초기화
app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:3000"])

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 파인튜닝된 모델 ID (파인튜닝 후 업데이트 필요)
FINE_TUNED_MODEL = "ft:gpt-3.5-turbo-0125:your-org-name::ftjob-HbdpEK5hHqlz9VEpgbEPJZj4"  # 여기에 파인튜닝된 모델 ID 입력

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the chatbot API!"})

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # 사용자 메시지 추출
        user_input = request.json.get("message", "")
        
        # 파인튜닝된 모델로 응답 생성
        response = client.chat.completions.create(
            model=FINE_TUNED_MODEL,  # 파인튜닝된 모델 사용
            messages=[
                {"role": "system", "content": "넌 인천대학교 챗봇이야. 학생들의 질문에 친절하고 정확하게 답변해줘."},
                {"role": "user", "content": user_input},
            ],
            temperature=0.7,
            max_tokens=300,  # 토큰 제한 설정
        )

        # 생성된 답변 반환
        reply = response.choices[0].message.content
        return jsonify({"response": reply})

    except Exception as e:
        app.logger.error(f"Error in chat endpoint: {str(e)}")
        return jsonify({"error": "서버 내부 오류가 발생했습니다."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)