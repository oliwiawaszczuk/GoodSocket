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
            store.setState({
                connectionState: "disconnected",
                loginState: "not-login",
            });
        });

         this.chatSocket.on("success-login", (data) => {
            console.log(data);
            store.setState({
                currentPage: 'chat',
                loginState: "login",
                error: null,
                username: data.username,
                userCode: data.userCode,
                sid: data.sid,
            });
        });

        this.chatSocket.on("failed-login", (error) => {
            store.setState({
                error: error,
            });
        });
    }

    public message(messageText: string) {
        if (!this.chatSocket) return;
        this.chatSocket.emit("message", messageText)
    }

    public auto_login(token: string | null) {
        if (!this.chatSocket) return;
        this.chatSocket.emit("auto_login", token);
    }

    public login(email: string, password: string) {
        if (!this.chatSocket) return;
        this.chatSocket.emit("login", {'email': email, 'password': password});
    }
    public register(username: string, email: string, password: string) {
        if (!this.chatSocket) return;
        this.chatSocket.emit("register", {'username': username, 'email': email, 'password': password});
    }

    public logout() {
        if (!this.chatSocket) return;
        this.chatSocket.emit("logout");
    }
}
