import axios from "axios";
import type { NextPage } from "next";
import Head from "next/head";
import { useState } from "react";

const serverUrl = "https://server/";
const Home: NextPage = () => {
  const [url, setUrl] = useState("");
  const [length, setLength] = useState(1024);
  const [loading, setLoading] = useState(false);

  const generate = () => {
    axios.get(`${serverUrl}/generate?length=${length}`).then((res) => {
      console.log(res);
    });
    setUrl("abc");
  };
  const download = () => {
    alert("generate!");
    setUrl("");
  };
  return (
    <>
      <Head>
        <title>CQTRNG | RNGaaS</title>
        <link rel="shortcut icon" href="https://i.ibb.co/J2tNZ3R/image.png" />
      </Head>
      <section
        className="w-full px-6 pb-12 antialiased bg-white"
        data-tails-scripts="//unpkg.com/alpinejs"
      >
        <div className="mx-auto max-w-7xl">
          <nav
            className="relative z-50 h-24 select-none"
            x-data="{ showMenu: false }"
          >
            <div className="container relative flex flex-wrap items-center justify-between h-24 mx-auto overflow-hidden font-medium border-b border-gray-200 md:overflow-visible lg:justify-center sm:px-4 md:px-2 lg:px-0">
              <div className="flex items-center justify-start w-1/4 h-full pr-4">
                <a href="#_" className="inline-block py-4 md:py-0">
                  <span className="p-1 text-xl font-black leading-none text-gray-900">
                    CQTRNG.
                  </span>
                </a>
              </div>
              <div className="top-0 left-0 items-start hidden w-full h-full p-4 text-sm bg-gray-900 bg-opacity-50 md:items-center md:w-3/4 md:absolute lg:text-base md:bg-transparent md:p-0 md:relative md:flex">
                <div className="flex-col w-full h-auto overflow-hidden bg-white rounded-lg md:bg-transparent md:overflow-visible md:rounded-none md:relative md:flex md:flex-row">
                  <a
                    href="#_"
                    className="inline-flex items-center block w-auto h-16 px-6 text-xl font-black leading-none text-gray-900 md:hidden"
                  >
                    CQTRNG<span className="text-indigo-600">.</span>
                  </a>
                  <div className="flex flex-col items-start justify-center w-full space-x-6 text-center lg:space-x-8 md:w-2/3 md:mt-0 md:flex-row md:items-center">
                    <a
                      href="#_"
                      className="inline-block w-full py-2 mx-0 ml-6 font-medium text-left text-indigo-600 md:ml-0 md:w-auto md:px-0 md:mx-2 lg:mx-3 md:text-center"
                    >
                      Home
                    </a>
                    <a
                      href="#_"
                      className="inline-block w-full py-2 mx-0 font-medium text-left text-gray-700 md:w-auto md:px-0 md:mx-2 hover:text-indigo-600 lg:mx-3 md:text-center"
                    >
                      Features
                    </a>
                    <a
                      href="#_"
                      className="inline-block w-full py-2 mx-0 font-medium text-left text-gray-700 md:w-auto md:px-0 md:mx-2 hover:text-indigo-600 lg:mx-3 md:text-center"
                    >
                      Pricing
                    </a>
                    <a
                      href="#_"
                      className="inline-block w-full py-2 mx-0 font-medium text-left text-gray-700 md:w-auto md:px-0 md:mx-2 hover:text-indigo-600 lg:mx-3 md:text-center"
                    >
                      Contact
                    </a>
                  </div>
                  <div className="flex flex-col items-start justify-end w-full pt-4 md:items-center md:w-1/3 md:flex-row md:py-0">
                    <a
                      href="#"
                      className="w-full px-3 py-2 mr-0 text-gray-700 md:mr-2 lg:mr-3 md:w-auto"
                    >
                      Sign In
                    </a>
                    <a
                      href="#_"
                      className="inline-flex items-center w-full px-6 py-3 text-sm font-medium leading-4 text-white bg-indigo-600 md:px-3 md:w-auto md:rounded-full lg:px-5 hover:bg-indigo-500 focus:outline-none md:focus:ring-2 focus:ring-0 focus:ring-offset-2 focus:ring-indigo-600"
                    >
                      Sign Up
                    </a>
                  </div>
                </div>
              </div>
              <div className="absolute right-0 flex flex-col items-center items-end justify-center w-10 h-10 bg-white rounded-full cursor-pointer md:hidden hover:bg-gray-100">
                <svg
                  className="w-6 h-6 text-gray-700"
                  x-show="!showMenu"
                  fill="none"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  x-cloak=""
                >
                  <path d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
                <svg
                  className="w-6 h-6 text-gray-700"
                  x-show="showMenu"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                  x-cloak=""
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M6 18L18 6M6 6l12 12"
                  ></path>
                </svg>
              </div>
            </div>
          </nav>

          <div className="container max-w-lg px-4 py-32 mx-auto mt-px text-left md:max-w-none md:text-center">
            <h1 className="text-5xl font-extrabold leading-10 tracking-tight text-left text-gray-900 md:text-center sm:leading-none md:text-6xl lg:text-7xl">
              <span className="inline md:block">Generate</span>{" "}
              <span className="relative mt-2 text-transparent bg-clip-text bg-gradient-to-br from-indigo-600 to-indigo-500 md:inline-block">
                Random Numbers
              </span>
            </h1>
            <div className="mx-auto mt-5 text-gray-500 md:mt-12 md:max-w-lg md:text-center lg:text-lg">
              We generate <strong>true, unbiased</strong> random number
              generator using a quantum device!
            </div>
            <div className="text-center text-sm text-gray-500 my-4">
              This is a demo, the website is not functional yet BUT you can
              scroll down and generate random numbers :).
            </div>
            <div className="flex flex-col items-center mt-12 text-center">
              <span className="relative inline-flex w-full md:w-auto">
                <a
                  href="#demo"
                  type="button"
                  className="inline-flex items-center justify-center w-full px-8 py-4 text-base font-bold leading-6 text-white bg-indigo-600 border border-transparent rounded-full md:w-auto hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-600"
                >
                  Try it for free
                </a>
              </span>
              <a href="#features" className="mt-3 text-sm text-indigo-500">
                Learn More
              </a>
            </div>
          </div>
        </div>
      </section>

      <section className="bg-gray-100">
        <div className="max-w-screen-xl px-4 py-12 mx-auto sm:px-6 lg:px-8">
          <div className="grid grid-cols-2 gap-8 md:grid-cols-3 lg:grid-cols-3">
            <div className="flex items-center justify-center col-span-1 md:col-span-2 lg:col-span-1">
              <img
                src="https://i.ibb.co/NCsWw9C/629a217b4ae75-image-removebg-preview.png"
                alt="Womanium's program logo"
                style={{ maxHeight: "100px", width: "auto" }}
              />
            </div>
            <div className="flex items-center justify-center col-span-1 md:col-span-2 lg:col-span-1">
              <img
                src="https://i.ibb.co/ChLyFKb/ORCA-Computing-Logo.png"
                alt="ORCA's logo"
                style={{ maxHeight: "100px", width: "auto" }}
              />
            </div>
            <div className="flex items-center justify-center col-span-1 md:col-span-2 lg:col-span-1">
              <img
                src="https://i.ibb.co/J2tNZ3R/image.png"
                alt="CQT's logo"
                style={{ maxHeight: "100px", width: "auto" }}
              />
            </div>
          </div>
        </div>
      </section>

      <section
        id="demo"
        className="py-8 leading-7 text-gray-900 bg-white sm:py-12 md:py-16 lg:py-24  "
      >
        <div
          className="max-w-6xl px-4 px-10 mx-auto border-solid lg:px-12 flex flex-col justify-center"
          style={{ minHeight: "400px" }}
        >
          <div className="leading-7 text-gray-900 border-0 border-gray-200">
            <div className="box-border text-center border-solid sm:text-left">
              <h2 className="m-0 mb-4 text-4xl font-semibold leading-tight tracking-tight text-left text-black border-0 border-gray-200 sm:text-5xl">
                Try it now
              </h2>
              <p className="mt-2 text-xl text-left text-gray-900 border-0 border-gray-200 sm:text-lg mb-4">
                Generate a random bitstring of length:
              </p>
              <input
                value={length}
                onChange={(e) => setLength(parseInt(e.target.value))}
                type="number"
                placeholder="length"
                className="ml-0 px-5  py-4 mt-6 font-sans text-base border border-gray-800 leading-none rounded cursor-pointer md:w-auto lg:mt-0 sm:text-lg  md:text-xl"
              />
            </div>
            <div className="my-10">
              <button
                className="my-2 mr-2 inline-flex items-center justify-center w-full px-5 py-4 mt-6 font-sans text-base leading-none text-white no-underline bg-indigo-600 border border-indigo-600 border-solid rounded cursor-pointer md:w-auto lg:mt-0 hover:bg-indigo-700 hover:border-indigo-700 hover:text-white focus-within:bg-indigo-700 focus-within:border-indigo-700 focus-within:text-white sm:text-lg md:text-xl disabled:bg-gray-500  disabled:border-gray-500"
                disabled={url !== "" || loading}
                onClick={generate}
              >
                Generate
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="w-5 h-5 ml-2"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                  <polyline points="12,5 19,12 12,19"></polyline>
                </svg>
              </button>
              <button
                className="inline-flex items-center justify-center w-full px-5 py-4 mt-6 ml-0 font-sans text-base leading-none text-white no-underline bg-indigo-600 border border-indigo-600 border-solid rounded cursor-pointer md:w-auto lg:mt-0 hover:bg-indigo-700 hover:border-indigo-700 hover:text-white focus-within:bg-indigo-700 focus-within:border-indigo-700 focus-within:text-white sm:text-lg lg:ml-6 md:text-xl disabled:bg-gray-500  disabled:border-gray-500"
                disabled={url === ""}
                onClick={download}
              >
                Download
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="w-5 h-5 ml-2"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <line x1="10" y1="5" x2="10" y2="19"></line>
                  <polyline points="5,12 10,19 15,12 "></polyline>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </section>

      <section className="py-20 bg-gray-100" id="features">
        <div className="container max-w-6xl mx-auto">
          <h2 className="text-4xl font-bold tracking-tight text-center">
            Our Features
          </h2>
          <div className="grid grid-cols-4 gap-8 mt-10 sm:grid-cols-8 lg:grid-cols-12 sm:px-8 xl:px-0">
            <div className="relative flex flex-col items-center justify-between col-span-4 px-8 py-12 space-y-4 overflow-hidden bg-white sm:rounded-xl">
              <div className="p-3 text-white bg-blue-500 rounded-full">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="w-8 h-8 "
                  viewBox="0 0 24 24"
                  strokeWidth="1.5"
                  stroke="currentColor"
                  fill="none"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                  <path d="M14 3v4a1 1 0 0 0 1 1h4"></path>
                  <path d="M5 8v-3a2 2 0 0 1 2 -2h7l5 5v11a2 2 0 0 1 -2 2h-5"></path>
                  <circle cx="6" cy="14" r="3"></circle>
                  <path d="M4.5 17l-1.5 5l3 -1.5l3 1.5l-1.5 -5"></path>
                </svg>
              </div>
              <h4 className="text-xl font-medium text-gray-700">Safe</h4>
              <p className="text-base text-center text-gray-500">
                Our bitstring are generated using Quantum Technologies making
                them unreproducible and are delivered through secured
                communication channels.
              </p>
            </div>

            <div className="flex flex-col items-center justify-between col-span-4 px-8 py-12 space-y-4  bg-white sm:rounded-xl">
              <div className="p-3 text-white bg-blue-500 rounded-full">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="w-8 h-8 "
                  viewBox="0 0 24 24"
                  strokeWidth="1.5"
                  stroke="currentColor"
                  fill="none"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                  <path d="M14 3v4a1 1 0 0 0 1 1h4"></path>
                  <path d="M5 8v-3a2 2 0 0 1 2 -2h7l5 5v11a2 2 0 0 1 -2 2h-5"></path>
                  <circle cx="6" cy="14" r="3"></circle>
                  <path d="M4.5 17l-1.5 5l3 -1.5l3 1.5l-1.5 -5"></path>
                </svg>
              </div>
              <h4 className="text-xl font-medium text-gray-700">Unbiased</h4>
              <p className="text-base text-center text-gray-500">
                We utilize highly engineered post-processors to guarantee that
                our bitstrings are unbiased.
              </p>
            </div>

            <div className="flex flex-col items-center justify-between col-span-4 px-8 py-12 space-y-4  bg-white sm:rounded-xl">
              <div className="p-3 text-white bg-blue-500 rounded-full">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="w-8 h-8 "
                  viewBox="0 0 24 24"
                  strokeWidth="1.5"
                  stroke="currentColor"
                  fill="none"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                  <polyline points="12 3 20 7.5 20 16.5 12 21 4 16.5 4 7.5 12 3"></polyline>
                  <line x1="12" y1="12" x2="20" y2="7.5"></line>
                  <line x1="12" y1="12" x2="12" y2="21"></line>
                  <line x1="12" y1="12" x2="4" y2="7.5"></line>
                  <line x1="16" y1="5.25" x2="8" y2="9.75"></line>
                </svg>
              </div>
              <h4 className="text-xl font-medium text-gray-700">High rate</h4>
              <p className="text-base text-center text-gray-500">
                We can deliver bitstrings at a very high rate to fit your needs.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section className="box-border py-8 leading-7 text-gray-900 bg-white border-0 border-gray-200 border-solid sm:py-12 md:py-16 lg:py-24">
        <div className="box-border max-w-6xl px-4 pb-12 mx-auto border-solid sm:px-6 md:px-6 lg:px-4">
          <div className="flex flex-col items-center leading-7 text-center text-gray-900">
            <h2 className="box-border m-0 text-3xl font-semibold leading-tight tracking-tight text-black border-solid sm:text-4xl md:text-5xl">
              Pricing Options
            </h2>
            <p className="box-border mt-4 text-2xl leading-normal text-gray-900 border-solid">
              We have adequate plan for your company's needs
            </p>
          </div>
          <div className="grid max-w-md mx-auto mt-6 overflow-hidden leading-7 text-gray-900 border border-b-4 border-gray-300 border-blue-600 rounded-xl md:max-w-lg lg:max-w-none sm:mt-10 lg:grid-cols-3">
            <div className="flex flex-col justify-between box-border px-4 py-8 mb-6 text-center bg-white border-solid lg:mb-0 sm:px-4 sm:py-8 md:px-8 md:py-12 lg:px-10">
              <h3 className="m-0 text-2xl font-semibold leading-tight tracking-tight text-black border-0 border-solid sm:text-3xl md:text-4xl">
                Basic
              </h3>
              <p className="mt-3 leading-7 text-gray-900 border-0 border-solid">
                The basic plan is a good fit for smaller teams and startups.
              </p>
              <div className="flex items-center justify-center mt-6 leading-7 text-gray-900 border-0 border-solid sm:mt-8">
                <p className="box-border m-0 text-6xl font-semibold leading-normal text-center border-0 border-gray-200">
                  $0
                </p>
                <p className="box-border my-0 ml-4 mr-0 text-xs text-left border-0 border-gray-200">
                  limited to 2M bits <span className="block">per month</span>
                </p>
              </div>

              <button className="inline-flex items-center justify-center w-full py-3 mt-6 font-sans text-sm leading-none text-center text-blue-600 no-underline bg-transparent border border-b-2 border-blue-600 rounded-md cursor-pointer hover:bg-blue-600 hover:border-blue-600 hover:text-white sm:text-base sm:mt-8 md:text-lg">
                Select Plan
              </button>
            </div>
            <div className="flex flex-col justify-between box-border px-4 py-8 mb-6 text-center bg-gray-100 border border-gray-300 border-solid lg:mb-0 sm:px-4 sm:py-8 md:px-8 md:py-12 lg:px-10">
              <h3 className="m-0 text-2xl font-semibold leading-tight tracking-tight text-black border-0 border-solid sm:text-3xl md:text-4xl">
                Science
              </h3>
              <p className="mt-3 leading-7 text-gray-900 border-0 border-solid">
                The science plan is a good fit for scientific companies, who
                need high rate of uniform bitstrings.
              </p>
              <div className="flex items-center justify-center mt-6 leading-7 text-gray-900 border-0 border-solid sm:mt-8">
                <p className="box-border m-0 text-6xl font-semibold leading-normal text-center border-0 border-gray-200">
                  $19
                </p>
                <p className="box-border my-0 ml-4 mr-0 text-xs text-left border-0 border-gray-200">
                  per 100M bits <span className="block">per month</span>
                </p>
              </div>
              <button className="inline-flex items-center justify-center w-full py-3 mt-6 font-sans text-sm leading-none text-center text-white no-underline bg-blue-600 border-b-4 border-blue-700 rounded cursor-pointer hover:text-white sm:text-base sm:mt-8 md:text-lg">
                Select Plan
              </button>
            </div>
            <div className="flex flex-col justify-between box-border px-4 py-8 text-center bg-white border-solid sm:px-4 sm:py-8 md:px-8 md:py-12 lg:px-10">
              <h3 className="m-0 text-2xl font-semibold leading-tight tracking-tight text-black border-0 border-solid sm:text-3xl md:text-4xl">
                Lock
              </h3>
              <p className="mt-3 leading-7 text-gray-900 border-0 border-solid">
                The lock plan is a good fit for companies who need the safest
                bitstrings.
              </p>
              <div className="flex items-center justify-center mt-6 leading-7 text-gray-900 border-0 border-solid sm:mt-8">
                <p className="box-border m-0 text-6xl font-semibold leading-normal text-center border-0 border-gray-200">
                  $39
                </p>
                <p className="box-border my-0 ml-4 mr-0 text-xs text-center border-0 border-gray-200">
                  per 100M bits <span className="block">per month</span>
                </p>
              </div>
              <button className="inline-flex items-center justify-center w-full py-3 mt-6 font-sans text-sm leading-none text-center text-blue-600 no-underline bg-transparent border border-b-2 border-blue-600 rounded cursor-pointer hover:bg-blue-600 hover:border-blue-600 hover:text-white sm:text-base sm:mt-8 md:text-lg">
                Select Plan
              </button>
            </div>
          </div>
        </div>
      </section>

      <section className="text-gray-700 bg-white body-font">
        <div className="container flex flex-col items-center px-8 py-8 mx-auto max-w-7xl sm:flex-row">
          <a
            href="#_"
            className="text-xl font-black leading-none text-gray-900 select-none logo"
          >
            CQTRNG<span className="text-indigo-600">.</span>
          </a>
          <p className="mt-4 text-sm text-gray-500 sm:ml-4 sm:pl-4 sm:border-l sm:border-gray-200 sm:mt-0">
            © 2021 CQTRNG built using{" "}
            <a href="https://devdojo.com/tails" style={{ color: "blue" }}>
              Tailwindcss Page Builder
            </a>
          </p>
          <span className="inline-flex justify-center mt-4 space-x-5 sm:ml-auto sm:mt-0 sm:justify-start">
            <a
              href="https://github.com/CQTech-womanium-hackathon/Random-number-generation-using-boson-sampling---ORCA-Computing"
              className="text-gray-400 hover:text-gray-500"
            >
              <span className="sr-only">GitHub</span>
              <svg
                className="w-6 h-6"
                fill="currentColor"
                viewBox="0 0 24 24"
                aria-hidden="true"
              >
                <path
                  fillRule="evenodd"
                  d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"
                  clipRule="evenodd"
                ></path>
              </svg>
            </a>
          </span>
        </div>
      </section>
    </>
  );
};

export default Home;
