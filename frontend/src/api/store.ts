import { create } from "zustand"


export const store = create<{
    connectionState: "not-connected" | "connected" | "disconnected";
    loginState: "not-login" | "logging" | "login";
    currentPage: "chat" | "profile";
    username: string | null;
    userCode: number | null;
    error: string | null;
    token: string | null;
}>(() => {
    return {
        connectionState: "not-connected",
        loginState: "not-login",
        currentPage: "chat",
        username: null,
        userCode: null,
        error: null,
        token: null,
    };
});