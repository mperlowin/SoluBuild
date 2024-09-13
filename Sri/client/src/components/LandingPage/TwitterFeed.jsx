import React, { useState } from "react";
import TweetCard from "./TweetCard";

const tweets = [
  {
    id: 1,
    username: "The Lincoln Project",
    handle: "@ProjectLincoln",
    content:
      "Well...\nx.com/ProjectLincoln…\nThe Lincoln Project\n@ProjectLincoln\nA sneak preview of the\nKamala vs. Trump debate\nhttps://t.co/lbCy6ERIRj",
    date: "11 Sep 2024",
    image:
      "https://cdn.builder.io/api/v1/image/assets/TEMP/c60c052d282c5971024839bfe6474c56df5f31a164e957f9fa0538b25bb6ead5?placeholderIfAbsent=true&apiKey=553b31a98a6c4f6db980cd4c031d36cc",
  },
  {
    id: 2,
    username: "The Lincoln Project",
    handle: "@ProjectLincoln",
    content:
      "Kamala Harris did exactly what she needed to do at last night's debate. She showed the American people exactly what kind of candidate Donald Trump is, says LP Chief of Staff",
    date: "11 Sep 2024",
  },
  // Add more tweet objects as needed
];

const TWEETS_PER_PAGE = 2; // Adjust this to control how many tweets appear on each page

function TwitterFeed() {
  const [currentPage, setCurrentPage] = useState(1);

  // Calculate total pages
  const totalPages = Math.ceil(tweets.length / TWEETS_PER_PAGE);

  // Get the current set of tweets for the page
  const currentTweets = tweets.slice(
    (currentPage - 1) * TWEETS_PER_PAGE,
    currentPage * TWEETS_PER_PAGE
  );

  const handleNextPage = () => {
    if (currentPage < totalPages) {
      setCurrentPage((prevPage) => prevPage + 1);
    }
  };

  const handlePrevPage = () => {
    if (currentPage > 1) {
      setCurrentPage((prevPage) => prevPage - 1);
    }
  };

  return (
    <div className="flex flex-col grow shrink items-center self-start pt-6 min-w-[240px] w-[633px] max-md:max-w-full">
      <div className="flex overflow-hidden flex-col w-full max-w-[729px] max-md:max-w-full">
        <div className="flex flex-col items-start space-y-6">
          {currentTweets.map((tweet) => (
            <TweetCard key={tweet.id} {...tweet} />
          ))}
        </div>
      </div>

      {/* Pagination Controls */}
      <div className="flex justify-between items-center mt-4 w-full max-w-[729px]">
        <button
          onClick={handlePrevPage}
          disabled={currentPage === 1}
          className="px-4 py-2 text-sm bg-gray-200 rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          Previous
        </button>
        <span className="text-sm text-gray-600">
          Page {currentPage} of {totalPages}
        </span>
        <button
          onClick={handleNextPage}
          disabled={currentPage === totalPages}
          className="px-4 py-2 text-sm bg-gray-200 rounded disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
          Next
        </button>
      </div>
    </div>
  );
}

export default TwitterFeed;
