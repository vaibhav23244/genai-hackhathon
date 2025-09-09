import Navbar from "@/components/global/navbar";
import "./globals.css";
import type { Metadata } from "next";
import { Space_Grotesk } from "next/font/google";

const spaceGrotesk = Space_Grotesk({
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "ScholarsGPT - Simplifying Legal Complexity with AI",
  description:
    "An AI-powered solution that simplifies complex legal documents into clear, accessible guidance, empowering users to make informed decisions and reduce legal risks.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${spaceGrotesk.className} dark tracking-tight antialiased`}
      >
        <main>
          <Navbar />
          {children}
        </main>
      </body>
    </html>
  );
}
