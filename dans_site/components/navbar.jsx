import Link from 'next/link';

export const Navbar = () => {
  return (
    <>
      <nav className="bg-gray-800 p-4 z-50">
        <div className="container mx-auto flex items-center justify-between">
          <div>
            <Link href="/" className="text-white text-2xl font-bold">
              My Website
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
