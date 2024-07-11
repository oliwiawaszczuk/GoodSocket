'use client';

import React, { useState, useEffect } from "react";
import FriendItemToList from "./FriendItemToList";
import InvitationItemToList from "./InvitationItemToList";

interface InvitationItem {
    id: number;
    username: string;
    userCode: string;
}

interface FriendItem {
    id: number;
    username: string;
    userCode: string;
}

const FriendsListBox: React.FC = () => {
    const [friendsList, setFriendsList] = useState<FriendItem[]>([]);
    const [invitationsList, setInvitationsList] = useState<InvitationItem[]>([]);

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
            {invitationsList.map(item => (
                <InvitationItemToList key={item.id} id={item.id} username={item.username} userCode={item.userCode} />
            ))}
            {friendsList.map(item => (
                <FriendItemToList key={item.id} id={item.id} username={item.username} userCode={item.userCode} />
            ))}
        </div>
    );
};

export default FriendsListBox;
