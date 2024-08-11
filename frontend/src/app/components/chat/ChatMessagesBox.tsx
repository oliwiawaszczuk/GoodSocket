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
            <Message msg={msg} key={index}/>
        ))}
    </div>
    );
};

export default ChatMessagesBox;
