'use client';

import React, { useState, useEffect } from "react";
import FriendItemToList from "./FriendItemToList";
import InvitationItemToList from "./InvitationItemToList";
import {store} from "@/api/store";

const FriendsListBox: React.FC = () => {
    const storage = store();

    // useEffect(() => {
    //     chatSocket.emit('get_invitations');
    //
    //     chatSocket.on('invitations_list', (data: InvitationItem[]) => {
    //         setInvitationsList(data);
    //     });
    //
    //     return () => {
    //         chatSocket.off('invitations_list');
    //     };
    // }, []);
    //
    // useEffect(() => {
    //     chatSocket.emit('get_friends_list');
    //
    //     chatSocket.on('friends_list', (data: FriendItem[]) => {
    //         setFriendsList(data);
    //     });
    //
    //     return () => {
    //         chatSocket.off('friends_list');
    //     };
    // }, []);

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
