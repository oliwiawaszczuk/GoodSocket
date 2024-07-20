'use client'
import {ChatSocket} from "@/api";

const ProfilePage = () => {
    return (
        <div className='w-full h-screen flex justify-center items-center'>
            <h1>profile page</h1>
            <button onClick={()=>{ ChatSocket.instance().logout(sessionStorage.getItem("token")); sessionStorage.removeItem("token") }}>Logout</button>
        </div>
    )
}

export default ProfilePage