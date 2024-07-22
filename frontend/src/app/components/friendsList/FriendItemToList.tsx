'use client'


import React, {useState} from "react";
import {store} from "@/api/store";

interface DataInterface {
    id: number;
    username: string;
    userCode: string;
    conv_id: number;
}

const FriendItemToList: React.FC<DataInterface> = ({id, username, userCode, conv_id}) => {
    const [codeActive, setCodeActive] = useState(false);

    return (
        <div className='bg-b_blue_dark2 px-3 py-2 mt-2 border-b-2 border-r-2 border-b_blue_dark3 rounded-xl hover:cursor-pointer text-f_yellow'
             onMouseEnter={() => setCodeActive(true)}
             onMouseLeave={() => setCodeActive(false)}
             onClick={() => store.setState({currentConversationId: conv_id})}
        >
            {username}{codeActive && <span className='opacity-80 text-gray-400'>#{userCode}</span>}
        </div>
    );
};

export default FriendItemToList;
