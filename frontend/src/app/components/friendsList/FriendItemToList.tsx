'use client'


import React, {useState} from "react";

interface DataInterface {
    id: number;
    username: string;
    userCode: string;
}

const FriendItemToList: React.FC<DataInterface> = ({id, username, userCode}) => {
    const [codeActive, setCodeActive] = useState(false);

    return (
        <div className='bg-b_blue_dark2 px-3 py-2 mt-2 border-b-2 border-r-2 border-b_blue_dark3 rounded-xl hover:cursor-pointer text-f_yellow' onMouseEnter={() => setCodeActive(true)} onMouseLeave={() => setCodeActive(false)}>
            {username}{codeActive && <span className='opacity-80 text-gray-400'>#{userCode}</span>}
        </div>
    );
};

export default FriendItemToList;
