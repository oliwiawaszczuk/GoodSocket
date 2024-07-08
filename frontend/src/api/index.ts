import socketIOClient, {Socket} from 'socket.io-client';
import {store} from "@/api/store";


export class ChatSocket {
    chatSocket: Socket | undefined;
    static _instance: ChatSocket | undefined;
    connecting: boolean = false;

    private constructor() {}

    public static instance(): ChatSocket {
        if (ChatSocket._instance === undefined) {
            ChatSocket._instance = new ChatSocket();
        }
        return ChatSocket._instance;
    }

    public isConnected(): boolean {
        if (!this.chatSocket) {
            return false;
        }
        return this.chatSocket.connected;
    }

    public isConnecting(): boolean {
        return this.connecting;
    }

    public connect() {
        this.connecting = true;
        this.chatSocket = socketIOClient('http://127.0.0.1:5000', {
            transports: ['websocket'],
            upgrade: true,
            reconnection: false,
            reconnectionAttempts: 5,
            reconnectionDelay: 1000,
            timeout: 20000,
        });

        this.chatSocket.on("connect", () => {
            console.log("Connection opened");
            this.connecting = false;
            store.setState({ connectionState: "connected" });
        });

        this.chatSocket.on("disconnect", () => {
            console.log("Connection closed");
            this.connecting = false;
            store.setState({ connectionState: "disconnected" });
        });
    }

    public message(messageText: string) {
        if (!this.chatSocket) return;
        this.chatSocket.emit("message", messageText)
    }
}
