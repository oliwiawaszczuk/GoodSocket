'use client'


import "../../public/fontello/css/fontello.css";
import {useEffect} from "react";
import {ChatSocket} from "@/api";
import {store} from "@/api/store";
import LoginPage from "@/app/components/login/LoginPage";
import ChatPage from "@/app/components/chat/ChatPage";
import ProfilePage from "@/app/components/profile/ProfilePage";

export default function Home() {
    const storage = store();

    useEffect(() => {
        if (window !== undefined) {
            const chatSocket = ChatSocket.instance();
            if (!chatSocket.isConnected() && !chatSocket.isConnecting()) {
                chatSocket.connect();
                chatSocket.auto_login(sessionStorage.getItem("token"));
            }
        }
    }, []);

    useEffect(() => {
        if (storage.loginState === "login") {
            if (typeof storage.token === "string") {
                sessionStorage.setItem('token', storage.token);
            }
        }
    }, [storage.loginState, storage.token]);


    return (
        <div>
            {storage.connectionState === "connected" &&
                <>
                    {storage.loginState === "not-login" && <LoginPage/>}
                    {storage.loginState === "login" &&
                        <>
                            {storage.currentPage === "chat" && <ChatPage/>}
                            {storage.currentPage === "profile" && <ProfilePage/>}
                        </>
                    }
                </>
            }
            {storage.connectionState === "not-connected" && <div className='flex w-full h-screen justify-center items-center'>Connecting...</div>}
            {storage.connectionState === "disconnected" && <div className='flex w-full h-screen justify-center items-center'>Disconnected</div>}
        </div>
    );
}
