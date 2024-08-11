'use client'
import {ChatSocket} from "@/api";

const ProfilePage = () => {
    return (
        <div className='w-full h-screen flex justify-center items-center flex-col'>
            <h1 className='text-xl p-5'>profile page</h1>
            <button onClick={()=>{ ChatSocket.instance().logout(sessionStorage.getItem("token")); sessionStorage.removeItem("token") }}>Logout</button>
        </div>
    )
}

export default ProfilePage