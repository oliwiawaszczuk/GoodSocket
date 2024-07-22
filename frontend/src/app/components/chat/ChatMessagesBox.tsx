'use client'


import React, {useEffect, useState} from "react";
import Message from "./Message";
import {store} from "@/api/store";
import {ChatSocket} from "@/api";

interface IChatMessage {
    id: number;
    conversation_id: number;
    date_and_hour: Date;
    message: string;
    username: string;
}

const ChatMessagesBox: React.FC = () => {
    const [messages, setMessages] = useState<IChatMessage[]>([]);
    const storage = store();

    useEffect(() => {
        const chatSocket = ChatSocket.instance();

        const fetchMessages = () => {
            chatSocket.chatSocket?.emit('message', storage.currentConversationId);
        };

        const handleMessage = (data: { conv_id: number, messages: IChatMessage[] }) => {
            if (data.conv_id === storage.currentConversationId) {
                setMessages(data.messages);
            }
        };

        fetchMessages();

        chatSocket.chatSocket?.on('message', handleMessage);

        return () => {
            chatSocket.chatSocket?.off('message', handleMessage);
        };
    }, [storage.currentConversationId]);

    useEffect(() => {
        const chatContainer = document.getElementById('conversation-container');
        if (chatContainer) {
            chatContainer.scrollTop = chatContainer.scrollHeight;
        }
    }, [messages]);

    return (
    <div className='p-2 flex-1 overflow-y-auto'>
        {messages.map((msg, index) => (
            <div key={index} className="bg-b_blue_dark2 px-2 py-1 rounded-xl">
                <div className="text-gray-300 text-sm">
                    {new Date(msg.date_and_hour).toLocaleString()}
                </div>
                <div className="text-gray-400 mt-1">
                    <span className={storage.username === msg.username ? "text-blue-400" : "text-green-300"}> {msg.username}: </span> {msg.message}
                </div>
            </div>
        ))}
    </div>
    );
};

export default ChatMessagesBox;
