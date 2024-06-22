/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./frontend/**/*.html", "./static/js/*.js"],
  darkMode: "selector",
  theme: {
    extend: {
      dropShadow: {
        "3xl": "0 15px 15px rgba(190, 242, 100, 0.2)",
      },

      keyframes: {
        sliding: {
          "0%": {
            transform: "translate(500px,0)",
          },
          "70%": {
            transform: "translate(0,0)",
            transform: "scale(1.3)",
          },
          "100%": {
            transform: "scale(1)",
          },
        },
      },
      animation: {
        slide: "sliding 1s ease-in ",
      },
      colors: {
        main: "#518B56",
        accent: "#B8FFBE",
        primary: "#FF8600",
        dark: "#171717",
      },
      fontFamily: {
        workSans: ["Work Sans", "sans-serif"],
        lato: ["Lato", "sans-serif"],
      },
    },
    screens: {
      xs: "480px",
      ss: "620px",
      sm: "768px",
      md: "1060px",
      lg: "1200px",
      xl: "1700px",
      xss: "360px",
    },
  },
  plugins: [],
};
