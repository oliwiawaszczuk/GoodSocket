'use client'


import React from "react";
import ChatMessagesBox from "./ChatMessagesBox";
import ChatInput from "./ChatInput";
import {ChatSocket} from "@/api";

const ChatContainer: React.FC = () => {


  return (
      <div className="w-full h-full flex flex-col overflow-hidden">
          <div className="flex-1 overflow-auto">
              <ChatMessagesBox/>
              <button onClick={() => { ChatSocket.instance().message('444') }}>SEND MSG</button>
          </div>
          <div className="h-14 ms:h-30 flex-none">
              <ChatInput/>
          </div>
      </div>
  );
};

export default ChatContainer;
