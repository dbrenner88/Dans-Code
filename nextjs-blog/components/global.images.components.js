import Image from 'next/image';

const danImage = () => {
return (
    <Image
        src="#public/images/danb.jpg"
        height={50}
        width={50}
        alt="Dan Brenner"
    />
    );
};

export default danImage;

function learningWithDan() {
    return (
        <Image
            src="#public/images/danb.jpg" />

    );
}