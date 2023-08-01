import Head from 'next/head';
import { Navbar } from '../components/navbar';
import PropTypes from 'prop-types';
import styles from '../styles/layout.module.css'


const name = 'Dan Brenner';
export const siteTitle = "Dan's site";

export default function Layout({ children, home }) {
  return (
    <div className={styles.container}>
      <Head>
        <link rel="icon" href="/lwd.ico" />
        <meta
          name="description"
          content="Dan"
        />
        <meta name="og:title" content={siteTitle} />
      </Head>
      <body>
      <Navbar />
        {children}
        </body>
    </div>
  );
}

Layout.propTypes = {
  children: PropTypes.node.isRequired,
  home: PropTypes.bool,
};
