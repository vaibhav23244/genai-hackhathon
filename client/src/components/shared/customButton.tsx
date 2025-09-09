import React from "react";
import Link from "next/link";
import { Button } from "../ui/button";
import { LucideIcon } from "lucide-react";

interface CustomButtonProps {
  href: string;
  color: string;
  heading: string;
  icon: LucideIcon;
  subHeading: string;
}

const CustomButton: React.FC<CustomButtonProps> = ({
  href,
  color,
  heading,
  icon: Icon,
  subHeading,
}) => {
  return (
    <Button
      asChild
      size="lg"
      variant="outline"
      className="flex items-center gap-x-3 py-8"
    >
      <Link href={href}>
        <div
          style={{ backgroundColor: color }}
          className="flex h-10 w-10 items-center justify-center rounded-lg"
        >
          <Icon />
        </div>
        <div className="flex flex-col items-start">
          <span className="text-base font-semibold">{heading}</span>
          <span className="text-xs text-gray-400">{subHeading}</span>
        </div>
      </Link>
    </Button>
  );
};

export default CustomButton;
