// pages/index.tsx
import React from "react";
import type { NextPage } from "next";
import Header from "../components/Header";

const Home: NextPage = () => {
  return (
    <div className="">
      <div className="h-40 grid place-content-center bg-indigo-900 text-gray-50">
        <h1 className="text-2xl">Hello, world. Learn how to code</h1>
      </div>
      <Header />
      <div className="container mx-auto">
        <div className="p-4">
          <h2 className="font-bold text-lg">Recent Posts</h2>
          <p className="h-[2000px]">Some content</p>
        </div>
      </div>
    </div>
  );
};

export default Home;
