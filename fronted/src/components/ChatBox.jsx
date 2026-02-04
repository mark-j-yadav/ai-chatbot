import { useState } from "react";
import { sendMessage } from "../services/api";
import Message from "./Message";

export default function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMsg = { role: "user", text: input };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");
    setLoading(true);

    const res = await sendMessage(userMsg.text);

    setMessages((prev) => [
      ...prev,
      { role: "bot", text: res.reply },
    ]);
    setLoading(false);
  };

  return (
    <div className="flex flex-col h-[600px] w-full max-w-xl mx-auto bg-white rounded-2xl shadow-xl">
      
      {/* Header */}
      <div className="px-6 py-4 border-b text-lg font-semibold text-gray-800">
        AI Chatbot 🤖
      </div>

      {/* Messages */}
      <div className="flex-1 p-4 space-y-3 overflow-y-auto bg-gray-50">
        {messages.map((msg, i) => (
          <Message key={i} role={msg.role} text={msg.text} />
        ))}

        {loading && (
          <div className="text-sm text-gray-400 animate-pulse">
            AI is typing...
          </div>
        )}
      </div>

      {/* Input */}
      <div className="p-4 border-t flex gap-2">
        <input
          className="flex-1 px-4 py-2 border rounded-xl focus:outline-none focus:ring-2 focus:ring-brand"
          placeholder="Ask something..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
        />
        <button
          onClick={handleSend}
          className="bg-brand text-white px-5 py-2 rounded-xl hover:opacity-90 transition"
        >
          Send
        </button>
      </div>
    </div>
  );
}
