'use client'


import React, {useState} from "react";
import FriendsListBox from "./FriendsListBox";
import FriendsListInput from "./FriendsListInput";

const FriendsListContainer: React.FC = () => {

    return (
        <div className="w-full h-full flex flex-col overflow-hidden">
            <div className="flex-1 overflow-auto">
                <FriendsListBox/>
            </div>
            <div className="h-40 md:h-14 ms:h-44 flex-none">
                <FriendsListInput/>
            </div>
        </div>
    );
};

export default FriendsListContainer;
