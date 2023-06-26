/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['M PLUS Code Latin', 'sans-serif']
      },
      transform: ['hover', 'focus'],
      skew: ['hover', 'focus'],
      backgroundImage: {
        'bg-img': "url('../images/imageedit_6_2133960528.jpg')"
      }
    },
  },
  plugins: [],
}

