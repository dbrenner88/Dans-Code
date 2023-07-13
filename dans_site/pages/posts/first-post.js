import Link from 'next/link';
import Head from 'next/head';
import Layout from '../../components/global.layouts';

export default function FirstPost() {
    return(
        <Layout>
            <Head>
                <title>Learning & Growing</title>
            </Head>
            <h1>First Post </h1>
            <iframe src="https://www.learningwithdan.com/embed" 
                    width="800" 
                    height="220" 
                    style={{ border: "1px solid #EEE", background: "white" }}
                    frameborder="0">
                    </iframe>
      {/* <iframe src="https://www.learningwithdan.com/" width={500} height={200}></iframe> */}
        </Layout>
    ); 
}