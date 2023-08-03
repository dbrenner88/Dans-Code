import Link from 'next/link';
import Image from 'next/image';
import utilStyles from '../styles/utils.module.css';

export const Navbar = () => {
  return (
    <>
      <nav className="bg-cyan-800 p-4 z-50">
        <div className="container mx-auto flex items-center justify-between">
            <div className="container mx-auto flex justify-between items-center">
            <Link href="/" >
            <Image
                    priority
                    src="/images/profile.jpg"
                    className={utilStyles.borderCircle}
                    height={50}
                    width={50}
                    alt=""
            />
                   </Link>
                </div>
            <div className="flex space-x-4">
          <Link href="/" passHref>
            <div className="text-white cursor-pointer">Home</div>
          </Link>
          </div>
        </div>
      </nav>
    </>
  );
};

/*

export const Navbar = () => {
    return (
      <>
        <nav className='flex items-center flex-wrap bg-cyan-800 p-3 '>
          <Link href='/'>
                <Image
                    priority
                    src="/images/profile.jpg"
                    className={utilStyles.borderCircle}
                    height={50}
                    width={50}
                    alt=""
                  />
              <span className='text-xl text-white font-bold uppercase tracking-wide ml-2'>
                Dan Brenner
              </span>
          </Link>
        </nav>
      </>
    );
  };
*/
