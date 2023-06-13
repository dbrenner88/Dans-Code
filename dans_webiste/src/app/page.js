import React from 'react';
import Header from "../components/Header";

function classNames(...classes) {
  return classes.filter(Boolean).join(' ')
}

const HomePage = () => {
  return (
    <div className="">
    <div className="h-30 grid place-content-center bg-indigo-900 text-gray-50"> 
      <h1 className="text-3xl">Dan's Website</h1>
    </div>
    <Header />
    <div className="container mx-auto">
      <div className="p-4">
        <h2 className="font-bold text-lg">Learning with Dan</h2>
        <p className="h-[1000px]"> Come learn with me!</p>
      </div>
    </div>
    <div>
      <a href="https://www.learningwithdan.com" target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:text-blue-700">
        LearningWithDan.com
      </a>
    </div>
  </div>
  );
};

export default HomePage;