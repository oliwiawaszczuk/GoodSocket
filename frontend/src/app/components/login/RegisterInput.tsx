'use client'

import React, {FormEvent, useState} from 'react'

interface RegisterInputProps {
  setLogin: React.Dispatch<React.SetStateAction<boolean>>;
}

const RegisterInput: React.FC<RegisterInputProps> = ({setLogin}) => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [showPassword, setShowPassword] = useState(false);

    const handleSubmit = async (e: FormEvent) => {
        // e.preventDefault();
        //
        // chatSocket.emit('register', {username, email, password});
        //
        // chatSocket.on('login_failed', (error) => {
        //     setError(error);
        // });

    };

    return (
        <>
            <h1 className='font-bold m-1 ml-0 text-3xl'>Register</h1>
            <form onSubmit={handleSubmit}>
                <input className='w-full bg-b_blue_dark2 border-b_blue_dark3 rounded-md my-1 px-2 py-1' type="text" name="username" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} maxLength={20}/>
                <input className='w-full bg-b_blue_dark2 border-b_blue_dark3 rounded-md my-1 px-2 py-1' type="email" name="email" placeholder="E-mail" value={email} onChange={(e) => setEmail(e.target.value)} maxLength={30}/>
                <div className="relative">
                    <input className='w-full bg-b_blue_dark2 border-b_blue_dark3 rounded-md my-1 px-2 py-1' type={showPassword ? "text" : "password"} name="password" placeholder="Password" autoComplete="off" value={password} onChange={(e) => setPassword(e.target.value)} />
                    <i onClick={() => setShowPassword(!showPassword)} className={`${showPassword ? 'icon-eye-off' : 'icon-eye'} absolute right-2 top-1/2 transform -translate-y-1/2 bg-transparent border-none cursor-pointer text-f_yellow`} />
                </div>
                {error && (
                    <h5 style={{color: '#d14242', padding: 0, margin: 0, paddingBottom: '10px'}}>
                        {error}
                    </h5>
                )}
                <input type="submit" value="Register" className='hover:bg-[#f09144] bg-f_yellow text-white border-b_blue_dark2 cursor-pointer mt-2 px-4 py-1 rounded-md'/>
            </form>
            <p> Do you have an account? <a onClick={() => setLogin(true)} className='text-[#ff8928] cursor-pointer'>Login</a></p>
        </>
    )
}

export default RegisterInput