/**
 * This code was generated by Builder.io.
 */
import React from "react";

function SearchBar() {
  return (
    <div className="flex flex-col justify-center items-center w-full max-md:max-w-full">
      <div className="flex p-1.5 max-w-full bg-white rounded border border-solid border-slate-300 w-[433px]">
        <input
          type="text"
          placeholder="Search Lincoln Project"
          aria-label="Search Lincoln Project"
          className="flex overflow-hidden flex-col flex-1 shrink justify-center px-2.5 py-3 text-lg text-red-900 bg-white rounded border border-solid basis-0 border-slate-300 max-w-[433px] min-w-[48px] max-md:pr-5"
        />
        <button
          type="submit"
          aria-label="Submit search"
          className="flex flex-col items-start self-start pl-2.5 w-[72px]"
        >
          <div className="flex flex-col justify-center items-center px-5 py-3 bg-red-900 rounded w-[62px]">
            <img
              loading="lazy"
              src="https://cdn.builder.io/api/v1/image/assets/TEMP/412c0f9a1a4bf9cf49b473732792cd5f4711638a389e6384e5e99c979bf26e59?placeholderIfAbsent=true&apiKey=553b31a98a6c4f6db980cd4c031d36cc"
              alt="Search icon"
              className="object-contain w-full aspect-square"
            />
          </div>
        </button>
      </div>
    </div>
  );
}

export default SearchBar;