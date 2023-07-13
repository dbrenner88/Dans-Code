import Image from 'next/image'

function DanImage () {
  return (
    <Image
      src="/images/profile.jpg"
      height={50}
      width={50}
      alt="Dan Brenner" />
  )
}

export default DanImage

export const LearningWithDanImage = () => {
  return (
      <Image
        src="/images/lwd.jpg"
        alt="Learning With Dan"
      />
  )
}

export const LinkedInButton = () => {
  const linkedinUrl = 'https://www.linkedin.com/in/brennerdaniel/'

  return (
      <a href={linkedinUrl} target="_blank" rel="noopener noreferrer">
        <img
          src="/LI-In-Bug.png"
          alt="LinkedIn"
          width="30"
          height="30"
        />
      </a>
  )
}
