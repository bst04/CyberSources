import type { Config } from "tailwindcss";

export default {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
        'banner-start': "#1C00A6",
        'banner-end': "#F40008"
      },
      animation: {
        'bg-loop': 'bg-loop 4s ease infinite'
      },
      keyframes: {
        'bg-loop': {
          '0%': { 'background-position-x': '0%', 'background-position-y': '50%' },
          '50%': { 'background-position-x': '100%', 'background-position-y': '50%' },
          '100%': { 'background-position-x': '0%', 'background-position-y': '50%' },
        }
      }
    },
  },
  plugins: [],
} satisfies Config;
