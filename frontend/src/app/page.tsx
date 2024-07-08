'use client'


import {useEffect} from "react";
import {ChatSocket} from "@/api";
import {store} from "@/api/store";

export default function Home() {
    const storage = store()

    useEffect(() => {
        if (window !== undefined) {
            const chatSocket = ChatSocket.instance();
            if (!chatSocket.isConnected() && !chatSocket.isConnecting()) {
                chatSocket.connect();
            }
        }
    }, []);


    return (
        <div>
            {storage.connectionState === "connected" && <div>
                <button onClick={() => {
                    ChatSocket.instance().message("wiadomosc");
                }}>Send msg</button>
            </div>}
            {storage.connectionState === "not-connected" && <div>Connecting...</div>}
            {storage.connectionState === "disconnected" && <div>Disconnected</div>}
        </div>
    );
}
