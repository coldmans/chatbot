import React, { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState(""); // 사용자 입력
  const [response, setResponse] = useState(""); // API 응답

  const sendMessage = async () => {
    try {
      const res = await axios.post(
        "http://172.30.1.72:5000/chat",
        { message: message },
        {
          headers: {
            "Content-Type": "application/json",
          },
          withCredentials: true, // 크로스 도메인 요청 시 필요
        }
      );
      console.log("API 응답:", res.data);
      setResponse(res.data.response); // API 응답 저장
    } catch (error) {
      console.error("Error communicating with the server:", error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Chatbot</h1>
      <textarea
        rows="4"
        cols="50"
        placeholder="메시지를 입력하세요"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <br />
      <button onClick={sendMessage}>Send</button>
      <h2>Response:</h2>
      <p>{response}</p>
    </div>
  );
}

export default App;
