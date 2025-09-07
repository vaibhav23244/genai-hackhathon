import { Github } from "lucide-react";
import Link from "next/link";

const Navbar = () => {
  return (
    <header className="fixed top-0 left-0 z-50 w-full py-4">
      <nav className="mx-auto flex max-w-3xl items-center justify-between px-4 sm:px-6 lg:px-8">
        <h1 className="text-xl font-semibold">ScholarsGPT</h1>
        <Link
          href="https://github.com/vaibhav23244/genai-hackhathon.git"
          target="_blank"
          className="rounded-full p-2 transition-all duration-300 ease-in-out hover:bg-gray-200/10"
        >
          <Github />
        </Link>
      </nav>
    </header>
  );
};

export default Navbar;
