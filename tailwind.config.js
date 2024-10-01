/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./cart/**/*.{html,js,py}"],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
}

