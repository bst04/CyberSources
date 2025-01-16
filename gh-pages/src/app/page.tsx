import Image from "next/image";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen min-w-screen p-8 pb-20 gap-16 sm:px-20 bg-gradient-to-tr from-banner-start to-banner-end  font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col sm:items-start">
        <div className="bg-black/65 p-4 border-2 w-full rounded-md">
        <h1 className="text-xl sm:text-3xl lg:text-7xl font-black text-green-500" ><span className="text-white">./</span>cybersources</h1>
        <h6 className="text-[0.5rem] sm:text-lg font-thin text-gray-50">.a_curated_list_of_cybersecurity_tools_and_resources</h6>
        {/* <hr className="w-full h-2 my-8 border-0 bg-gradient-to-l from-banner-start to-banner-end motion-safe:animate-bg-loop bg-[length:120%_120%] "/> */}
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
