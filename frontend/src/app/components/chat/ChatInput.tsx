'use client'


import React, {useState} from "react";

const ChatInput: React.FC = () => {
  const [message, setMessage] = useState("");

    const sendMessage = () => {
        // socket.emit("message", { text: message, 'session': getCookie('session'), 'currentConversationId': currentConversationId });
        // setMessage("");
        // chatSocket.emit('check_sid', localStorage.getItem('token'))
    };

  return (
      <div className="flex h-full p-0 ms:flex-col">
        {/*  INPUT TEXT TO MESSAGE */}
        <div className="w-[75%] mf:w-[85%] ms:w-full p-1 h-full flex items-center ">
          <input
              type="text"
              className="flex-1 p-2.5 rounded-md text-base w-full text-text_yellow bg-f_yellow border-4 border-gray-800 placeholder:text-placeholder_dark text-b_blue_dark"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              placeholder="Type your message here..."
          />
        </div>
        {/*  BUTTON TO SEND MESSAGE */}
        <div className="w-[25%] mf:w-[15%] ms:w-full p-1 h-full flex items-center">
            <button
                className='px-5 py-2.5 rounded-md bg-f_yellow text-b_blue_dark w-full text-base cursor-pointer transition-colors duration-300 border-4 border-gray-800 hover:bg-f_yellow_dark'
                onClick={sendMessage}>
                Send <i className="icon-paper-plane"></i>
            </button>
        </div>
      </div>
  );
};

export default ChatInput;
