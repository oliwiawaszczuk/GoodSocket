import type {Config} from "tailwindcss";

const config: Config = {
    content: [
        "./src/**/*.{js,ts,jsx,tsx,mdx}",
        "./pages/**/*.{js,ts,jsx,tsx,mdx}",
        "./components/**/*.{js,ts,jsx,tsx,mdx}",
        "./app/**/*.{js,ts,jsx,tsx,mdx}",
    ],
    theme: {
        extend: {
            backgroundImage: {
                "gradient-radial": "radial-gradient(circle, #424769 0%, #333752 100%)",
                'gradient-left-top': 'linear-gradient(to left top, #1a1c30, #2D3250, #424769)',
                "gradient-conic": "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
            },
            height: {
                '30': '7.5rem',
            },
            colors: {
                f_yellow: '#F6B17A',
                f_yellow_dark: '#e69c5d',
                b_blue_dark: '#243142',
                b_blue_dark1: '#424769',
                b_blue_dark2: '#2D3250',
                b_blue_dark3: '#1d2132',
                placeholder_dark: 'rgba(36,49,66,0.73)',
                date_gray: 'rgba(200, 200, 202, 0.69)',
                username: 'rgba(111, 188, 100, 0.75)',
                username2: 'rgba(91, 192, 228, 0.75)',
            },
            screens: {
                'ms': {'max': '600px'},
                'md': '920px',
                'mf': '1250px',
                'mg': '1420px',
                'mx': '1720px',
            },
            boxShadow: {
                'light': '0 2px 4px rgba(255, 255, 255, 0.1)',
                'dark': '2px 2px 5px rgba(20, 20, 20, 0.5)',
            },
        },
    },
    plugins: [],
};
export default config;
