'use client'


import React, {useState} from "react";
import {store} from "@/api/store";

interface IChatMessage {
    id: number;
    conversation_id: number;
    date_and_hour: Date;
    message: string;
    username: string;
}

const Message: React.FC<{msg: IChatMessage}> = ({msg}) => {
    const storage = store();

    return (
        <div className="bg-b_blue_dark2 px-2 py-1 rounded-xl mt-2">
            <div className="text-gray-300 text-sm">
                {new Date(msg.date_and_hour).toLocaleString()}
            </div>
            <div className="text-gray-400 mt-1">
                <span className={storage.username === msg.username ? "text-blue-400" : "text-green-300"}> {msg.username}: </span> {msg.message}
            </div>
        </div>
    );
};

export default Message;
