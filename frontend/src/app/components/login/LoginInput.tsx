'use client'

import React, {FormEvent, useState} from 'react'
import {store} from "@/api/store";
import {ChatSocket} from "@/api";

interface LoginInputProps {
    setLogin: React.Dispatch<React.SetStateAction<boolean>>;
}

const LoginInput: React.FC<LoginInputProps> = ({setLogin}) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [showPassword, setShowPassword] = useState(false);
    const storage = store()

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();

        ChatSocket.instance().login(email, password);
    };

    return (
        <>
            <h1 className='font-bold m-1 ml-0 text-3xl'>Login</h1>
            <form onSubmit={handleSubmit}>
                <input className='w-full bg-b_blue_dark2 border-b_blue_dark3 rounded-md my-1 px-2 py-1' type="email"
                       name="email" placeholder="E-mail" value={email} onChange={(e) => setEmail(e.target.value)}/>
                <div className="relative">
                    <input className='w-full bg-b_blue_dark2 border-b_blue_dark3 rounded-md my-1 px-2 py-1'
                           type={showPassword ? "text" : "password"} name="password" placeholder="Password"
                           autoComplete="off" value={password} onChange={(e) => setPassword(e.target.value)}/>
                    <i onClick={() => setShowPassword(!showPassword)}
                       className={`${showPassword ? 'icon-eye-off' : 'icon-eye'} absolute right-2 top-1/2 transform -translate-y-1/2 bg-transparent border-none cursor-pointer text-f_yellow`}/>
                </div>
                {storage.error && (
                    <h5 style={{color: '#d14242', padding: 0, margin: 0, paddingBottom: '10px'}}>
                        {storage.error}
                    </h5>
                )}
                <input
                    className='hover:bg-[#f09144] bg-f_yellow text-white border-b_blue_dark2 cursor-pointer mt-2 px-4 py-1 rounded-md'
                    type="submit" value="Login"/>
            </form>
            <p> Don't have an account? <a onClick={() => setLogin(false)}
                                          className='text-[#ff8928] cursor-pointer'>Register</a></p>
        </>
    )
}

export default LoginInput