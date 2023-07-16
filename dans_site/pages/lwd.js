import React from 'react';
import Head from 'next/head';
import Layout from '../components/global.layouts.js';
import Image from 'next/image.js';

export default function LearningWithDan() {
  return (
    <Layout>
      <Head>
        <title>Learning & Growing</title>
      </Head>
      <h1>Learning With Dan Articles</h1>
      <h2>Multipliers - how you can help your teams grow</h2>
      <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <Image
          src="/images/multipliers.png"
          height={100}
          width={200}
          alt="Multipliers"
        />
      </div>
      <iframe
        src="https://www.learningwithdan.com/embed"
        width="800"
        height="170"
        style={{
          border: '1px solid #EEE',
          background: 'white',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      ></iframe>
    </Layout>
  );
}
