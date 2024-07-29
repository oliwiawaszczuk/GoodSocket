import socketIOClient, { Socket } from "socket.io-client";
import { store } from "@/api/store";

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
    this.chatSocket = socketIOClient("http://127.0.0.1:5000", {
      transports: ["websocket"],
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

      this.getInvitations();
      this.getFriendsList();
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
        currentPage: "chat",
        loginState: "login",
        error: null,
        username: data.username,
        userCode: data.userCode,
        token: data.token,
      });
    });

    this.chatSocket.on("failed-login", (error) => {
      store.setState({
        error: error,
      });
    });

    this.chatSocket.on("invitations_list", (data: InvitationItem[]) => {
      console.log("Got invitations list!", data);
      store.setState({ invitationsList: data, error: null });
    });

    this.chatSocket.on("friends_list", (data: FriendItem[]) => {
      console.log("Got friends list!", data);
      store.setState({ friendsList: data, error: null });
    });

    this.chatSocket.on("failed_request_end_with_error", (error) => {
      store.setState({
        error: error,
      });
    });
  }

  public new_message(messageText: string) {
    if (!this.chatSocket) return;
    this.chatSocket.emit("add_new_message", { text: messageText, conv_id: store.getState().currentConversationId });
  }

  public auto_login(token: string | null) {
    if (!this.chatSocket) return;
    this.chatSocket.emit("auto_login", token);
  }

  public login(email: string, password: string) {
    if (!this.chatSocket) return;
    this.chatSocket.emit("login", { email: email, password: password });
  }

  public register(username: string, email: string, password: string) {
    if (!this.chatSocket) return;
    this.chatSocket.emit("register", { username: username, email: email, password: password });
  }

  public logout(token: string | null) {
    if (!this.chatSocket) return;
    this.chatSocket.emit("logout", { token: token });
    store.setState({
      loginState: "not-login",
      error: "",
      currentPage: "chat",
      username: null,
      userCode: null,
    });
  }

  private getInvitations() {
    if (!this.chatSocket) return;
    this.chatSocket.emit("get_invitations");
  }

  private getFriendsList() {
    if (!this.chatSocket) return;
    this.chatSocket.emit("get_friends_list");
  }

  public AddNewInvitation(inputValue: string | null) {
    if (!this.chatSocket) return;
    this.chatSocket.emit("add_new_invitation", inputValue);
  }

  public AcceptInvitation(id: number | null) {
    if (!this.chatSocket) return;
    this.chatSocket.emit("accept_invitation", id);
  }

  public DeclineInvitation(id: number | null) {
    if (!this.chatSocket) return;
    this.chatSocket.emit("decline_invitation", id);
  }
}
