'use client'


import React, {useState} from "react";

const FriendsListInput: React.FC = () => {
    const [inputValue, setInputValue] = useState("");

    const AddNewFriend = () => {

    }

    return (
      <div className="flex h-full p-0 ms:flex-col">
          {/*  INPUT TEXT TO ADD NEW FRIEND */}
          <div className="w-[65%] mf:w-[65%] ms:w-full p-1  flex items-center ">
              <input
                  type="text"
                  className="flex-1 p-2.5 rounded-md text-base w-full text-text_yellow bg-f_yellow border-4 border-gray-800 placeholder:text-placeholder_dark text-b_blue_dark"
                  value={inputValue}
                  onChange={(e) => setInputValue(e.target.value)}
                  placeholder="Type user#code here..."
              />
          </div>
          {/*  BUTTON TO ADD NEW FRIEND */}
          <div className="w-[35%] mf:w-[35%] ms:w-full p-1  flex items-center">
              <button
                  className='px-2 py-2.5 rounded-md bg-f_yellow text-b_blue_dark w-full text-base cursor-pointer transition-colors duration-300 border-4 border-gray-800 hover:bg-f_yellow_dark'
                  onClick={AddNewFriend}>
                  Add <i className="icon-user-plus"></i>
              </button>
          </div>
      </div>
    );
};

export default FriendsListInput;
