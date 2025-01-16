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
        'banner-start': "var(--bstart)",
        'banner-end': "var(--bend)"
      },
      animation: {
        'bg-loop': 'bg-loop 4s ease infinite',
        'shadow-loop': 'shadow-loop 4s ease infinite'
      },
      keyframes: {
        'bg-loop': {
          '0%': { 'background-position-x': '0%', 'background-position-y': '50%',  'box-shadow': "var(--bstart) -2px 5px 15px" },
          '50%': { 'background-position-x': '100%', 'background-position-y': '50%', 'box-shadow': "var(--bend) -2px 5px 15px" },
          '100%': { 'background-position-x': '0%', 'background-position-y': '50%', 'box-shadow': "var(--bstart) -2px 5px 15px" },
        },
        'shadow-loop': {
          '0%': { 'shadow': "var(--bstart) 0px 5px 15px"},
          '100%': { 'shadow': "var(--bend) 0px 5px 15px"},
        }
      }
    },
  },
  plugins: [],
} satisfies Config;
