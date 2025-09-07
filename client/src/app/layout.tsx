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
        <div className="relative min-h-screen w-full overflow-hidden">
          <div
            className="pointer-events-none absolute inset-0 z-0"
            style={{
              background: `
        radial-gradient(
          circle at center,
          rgba(59, 130, 246, 0.12) 0%,
          rgba(59, 130, 246, 0.06) 20%,
          rgba(0, 0, 0, 0.0) 60%
        )
      `,
            }}
          />
          <main>
            <Navbar />
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}
