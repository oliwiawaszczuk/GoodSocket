import { create } from "zustand"


export const store = create<{
    connectionState: "not-connected" | "connected" | "disconnected";
}>(() => {
    return {
        connectionState: "not-connected",
    };
});