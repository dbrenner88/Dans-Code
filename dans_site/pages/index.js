import Link from 'next/link';
import Head from 'next/head';
import Layout, { siteTitle } from '../components/global.layouts';
import utilStyles from '../styles/utils.module.css';

export default function Home() {
  return (
    <Layout home>
      <Head>
        <title>{siteTitle}</title>
      </Head>
      <section className={utilStyles.headingMd}>
        <p>Hi, I'm <b>Dan</b> and I love to learn. Check me out on&nbsp; 
        <a href="https://www.learningwithdan.com" 
           target="_blank"
           style={{ color: '#009074' }}
           > 
           Learning With Dan</a> 
           &nbsp;and come learn with me! 
           </p>
        <p>
        <Link href= "/posts/first-post"> 
          Come checkout my first post! 
          </Link>
        </p>
      </section>
    </Layout>
  );
}