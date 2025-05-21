module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        black: "#000000",
        white: "#ffffff",
        accent: "#ff00ff"
      },
      fontFamily: {
        brutal: ["'Courier New'", "monospace"]
      }
    }
  },
  plugins: []
};
