import {create} from "zustand"

interface InvitationItem {
    id: number;
    username: string;
    userCode: string;
}

interface FriendItem {
    id: number;
    username: string;
    userCode: string;
    conv_id: number;
}

export const store = create<{
    connectionState: "not-connected" | "connected" | "disconnected";
    loginState: "not-login" | "logging" | "login";
    currentPage: "chat" | "profile";
    username: string | null;
    userCode: number | null;
    error: string | null;
    token: string | null;

    currentConversationId: number;

    invitationsList: InvitationItem[];
    friendsList: FriendItem[];
}>(() => {
    return {
        connectionState: "not-connected",
        loginState: "not-login",
        currentPage: "chat",
        username: null,
        userCode: null,
        error: null,
        token: null,

        currentConversationId: 0,

        invitationsList: [],
        friendsList: [],
    };
});