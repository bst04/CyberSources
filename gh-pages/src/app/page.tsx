import Image from "next/image";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen min-w-screen gap-16  bg-gray-900  font-[family-name:var(--font-geist-sans)]">
      <div className="flex flex-row gap-8 items-center bg-black/65 w-full p-8">
        <div className="relative h-16 aspect-square">
          <Image className="rounded-md left-0" src="/cybersources/logo.svg" fill={true} alt="logo"/>
        </div>
        <div className="">
          <h2 className="text-xl sm:text-3xl lg:text-7xl font-black text-green-500" ><span className="text-white">./</span>cybersources</h2>
          {/* <hr className="w-full h-2 my-8 border-0 bg-gradient-to-l from-banner-start to-banner-end motion-safe:animate-bg-loop bg-[length:120%_120%] "/> */}
        </div>
      </div>
      <main className="flex flex-col items-center gap-16 px-8  pb-20">
        <h2 className="text-xl lg:max-w-[50%] sm:text-5xl font-black text-center text-gray-50">A curated list of cybersecurity tools and resources</h2>
        <div className="rounded-md p-[3px] bg-gradient-to-r from-banner-start to-banner-end focus-within:motion-safe:animate-bg-loop bg-[length:120%_120%]">
          <input className="w-80 bg-gray-900 p-2 rounded-md focus:outline-none" placeholder="read input | xargs find -t l {} ."/>
        </div>
      </main>
      <footer className="mt-auto row-start-3 flex gap-6 flex-wrap items-center justify-center">
        <a
          className="flex items-center gap-2 hover:underline hover:underline-offset-4"
          href="https://nextjs.org/learn?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Image
            aria-hidden
            src="/cybersources/file.svg"
            alt="File icon"
            width={16}
            height={16}
          />
          Learn
        </a>
        <a
          className="flex items-center gap-2 hover:underline hover:underline-offset-4"
          href="https://vercel.com/templates?framework=next.js&utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Image
            aria-hidden
            src="/cybersources/window.svg"
            alt="Window icon"
            width={16}
            height={16}
          />
          Examples
        </a>
        <a
          className="flex items-center gap-2 hover:underline hover:underline-offset-4"
          href="https://nextjs.org?utm_source=create-next-app&utm_medium=appdir-template-tw&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Image
            aria-hidden
            src="/cybersources/globe.svg"
            alt="Globe icon"
            width={16}
            height={16}
          />
          Go to nextjs.org →
        </a>
      </footer>
    </div>
  );
}
