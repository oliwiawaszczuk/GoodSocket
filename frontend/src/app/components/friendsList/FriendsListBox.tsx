'use client';

import React, { useState, useEffect } from "react";
import FriendItemToList from "./FriendItemToList";
import InvitationItemToList from "./InvitationItemToList";
import {store} from "@/api/store";

const FriendsListBox: React.FC = () => {
    const storage = store();

    return (
        <div>
            {storage.invitationsList.map(item => (
                <InvitationItemToList key={item.id} id={item.id} username={item.username} userCode={item.userCode} />
            ))}
            {storage.friendsList.map(item => (
                <FriendItemToList key={item.id} id={item.id} username={item.username} userCode={item.userCode} conv_id={item.conv_id}/>
            ))}
        </div>
    );
};

export default FriendsListBox;
