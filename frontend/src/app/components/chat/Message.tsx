'use client'


import React, {useState} from "react";

const Message: React.FC = () => {

    return (
        <div className="bg-b_blue_dark2 p-2 px-3 rounded-xl drop-shadow-md">
            <div className="text-date_gray">12.06.2024 12:36:23</div>
            <div className="text-f_yellow"> <span className="text-username2">Kto pisze: </span>Wiadomosc</div>
        </div>
    );
};

export default Message;
