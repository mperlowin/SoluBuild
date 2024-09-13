import React from "react";

function TweetCard({ username, handle, content, date, image }) {
  return (
    <div className="flex flex-col w-full p-5 bg-white rounded-lg shadow-lg border border-gray-200 max-w-xl mx-auto hover:shadow-xl transition-shadow duration-300 ease-in-out">
      {/* Header Section */}
      <div className="flex items-center mb-4">
        <img
          loading="lazy"
          src="https://cdn.builder.io/api/v1/image/assets/TEMP/0754b4f8d167fca1961e005f3b001ecac3a13ccc1d2fe459b17abaf599ab66bc?placeholderIfAbsent=true&apiKey=553b31a98a6c4f6db980cd4c031d36cc"
          alt={`${username}'s profile picture`}
          className="w-12 h-12 rounded-full object-cover mr-3"
        />
        <div className="flex flex-col">
          <span className="text-lg font-semibold text-black">{username}</span>
          <span className="text-gray-500">{handle}</span>
        </div>
        <img
          src="https://cdn.builder.io/api/v1/image/assets/TEMP/1772d38210e8cbf52ef2a37ccb9db635edc1802224abf109fff2619b01e612be?placeholderIfAbsent=true&apiKey=553b31a98a6c4f6db980cd4c031d36cc"
          alt="Twitter verified badge"
          className="ml-auto w-6 h-6"
        />
      </div>

      {/* Tweet Content */}
      <div className="mb-4">
        <p className="text-base text-gray-900 leading-relaxed">{content}</p>
        {image && (
          <img
            loading="lazy"
            src={image}
            alt="Tweet image"
            className="mt-3 rounded-lg w-full object-cover max-h-96"
          />
        )}
      </div>

      {/* Interaction Section */}
      <div className="flex items-center justify-between text-gray-500 text-sm mt-2">
        <div className="flex items-center gap-4">
          <img
            loading="lazy"
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/8d09ed3768cef2af6366fd1ac42762f7fd2e536fe49f1079bce5d0b579074d3d?placeholderIfAbsent=true&apiKey=553b31a98a6c4f6db980cd4c031d36cc"
            alt="Reply icon"
            className="w-5 h-5 cursor-pointer hover:text-blue-500"
          />
          <img
            loading="lazy"
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/3d09a453a66a114360d6b3be93a8aff76a36fb4a801af93b8ab3777ff95c2e18?placeholderIfAbsent=true&apiKey=553b31a98a6c4f6db980cd4c031d36cc"
            alt="Retweet icon"
            className="w-5 h-5 cursor-pointer hover:text-green-500"
          />
          <img
            loading="lazy"
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/e120bd2d83afdb8bf8e649f3dbcb3c2ad1817d3fe23e046f150d4f1a6bb79c38?placeholderIfAbsent=true&apiKey=553b31a98a6c4f6db980cd4c031d36cc"
            alt="Like icon"
            className="w-5 h-5 cursor-pointer hover:text-red-500"
          />
        </div>
        <span className="text-xs text-gray-400">{date}</span>
      </div>
    </div>
  );
}

export default TweetCard;
