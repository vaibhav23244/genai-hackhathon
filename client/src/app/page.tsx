import Link from "next/link";
import CustomButton from "@/components/shared/customButton";
import { ArrowUpRight, Eye, FileText } from "lucide-react";

const Home = () => {
  return (
    <div className="h-screen w-full overflow-hidden">
      <div className="relative isolate px-6 lg:px-8">
        <div
          aria-hidden="true"
          className="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80"
        >
          <div
            style={{
              clipPath:
                "polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)",
            }}
            className="relative left-[calc(50%-11rem)] aspect-1155/678 w-144.5 -translate-x-1/2 rotate-30 bg-linear-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%-30rem)] sm:w-288.75"
          />
        </div>
        <div className="mx-auto max-w-2xl py-24 sm:py-36">
          <div className="hidden sm:mb-8 sm:flex sm:justify-center">
            <div className="shimmer relative rounded-full px-3 py-1 text-sm/6 text-gray-600 ring-1 ring-gray-900/10 hover:ring-gray-900/20 dark:text-gray-400 dark:ring-white/10 dark:hover:ring-white/20">
              New: Smarter contract reviews powered by AI.{" "}
              <Link
                href="#"
                className="group inline-flex items-center font-semibold text-gray-200"
              >
                <span aria-hidden="true" className="absolute inset-0" />
                Try it now{" "}
                <ArrowUpRight className="ml-1 h-4 w-4 transition-all duration-300 ease-in-out group-hover:rotate-45" />
              </Link>
            </div>
          </div>
          <div className="text-center">
            <h1 className="text-balanced text-5xl font-semibold tracking-tight sm:text-6xl">
              Understand legal documents instantly.
            </h1>
            <p className="mt-8 text-lg font-medium text-pretty text-gray-400 sm:text-xl">
              Our AI-powered analyzer simplifies complex legal jargon,
              highlights risks, and saves hours of manual reading — so you focus
              on making better decisions.
            </p>
            <div className="mt-10 flex items-center justify-center gap-x-6">
              <CustomButton
                href="#"
                color="#1C1034"
                icon={FileText}
                heading="Analyze Document"
                subHeading="Get instant AI insights"
              />
              <CustomButton
                href="#"
                icon={Eye}
                color="#310A1F"
                heading="Live Demo"
                subHeading="Experience it in action"
              />
            </div>
            <div
              aria-hidden="true"
              className="absolute inset-x-0 top-[calc(100%-13rem)] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[calc(100%-30rem)]"
            >
              <div
                style={{
                  clipPath:
                    "polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)",
                }}
                className="relative left-[calc(50%+3rem)] aspect-1155/678 w-144.5 -translate-x-1/2 bg-linear-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%+36rem)] sm:w-288.75"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
