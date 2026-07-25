/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './*/templates/**/*.html',
    './static/js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        // ------------------------------------------------------------------
        // Bảng màu đầy đủ theo DESIGN.md (Heritage Narrative System).
        // Giữ nguyên tên key = tên token trong DESIGN.md để có thể copy
        // nguyên class từ file thiết kế (Stitch) mà không cần đổi tên.
        // ------------------------------------------------------------------
        surface: '#f9f9f9',
        'surface-dim': '#dadada',
        'surface-bright': '#f9f9f9',
        'surface-container-lowest': '#ffffff',
        'surface-container-low': '#f3f3f4',
        'surface-container': '#eeeeee',
        'surface-container-high': '#e8e8e8',
        'surface-container-highest': '#e2e2e2',
        'on-surface': '#1a1c1c',
        'on-surface-variant': '#41484a',
        'inverse-surface': '#2f3131',
        'inverse-on-surface': '#f0f1f1',
        outline: '#71787b',
        'outline-variant': '#c1c8ca',
        'surface-tint': '#3d6470',

        primary: '#002d37',
        'on-primary': '#ffffff',
        'primary-container': '#1a434e',
        'on-primary-container': '#88afbc',
        'inverse-primary': '#a5cdda',

        secondary: '#4a654e',
        'on-secondary': '#ffffff',
        'secondary-container': '#c9e8cb',
        'on-secondary-container': '#4e6952',

        tertiary: '#282825',
        'on-tertiary': '#ffffff',
        'tertiary-container': '#3e3e3b',
        'on-tertiary-container': '#aaa9a5',

        error: '#ba1a1a',
        'on-error': '#ffffff',
        'error-container': '#ffdad6',
        'on-error-container': '#93000a',

        'primary-fixed': '#c0e9f7',
        'primary-fixed-dim': '#a5cdda',
        'on-primary-fixed': '#001f27',
        'on-primary-fixed-variant': '#244c57',

        'secondary-fixed': '#cceace',
        'secondary-fixed-dim': '#b0ceb2',
        'on-secondary-fixed': '#07200f',
        'on-secondary-fixed-variant': '#334d38',

        'tertiary-fixed': '#e4e2dd',
        'tertiary-fixed-dim': '#c8c6c2',
        'on-tertiary-fixed': '#1b1c19',
        'on-tertiary-fixed-variant': '#474744',

        background: '#f9f9f9',
        'on-background': '#1a1c1c',
        'surface-variant': '#e2e2e2',
      },
      fontFamily: {
        // Alias tiện dùng (giữ từ Task 1.2)
        heading: ['Literata', 'serif'],
        sans: ['Hanken Grotesk', 'sans-serif'],
        // Tên token typography trong DESIGN.md — dùng chung với fontSize bên dưới,
        // vd: class="font-display-lg text-display-lg"
        'display-lg': ['Literata', 'serif'],
        'display-md': ['Literata', 'serif'],
        'headline-lg': ['Literata', 'serif'],
        'headline-lg-mobile': ['Literata', 'serif'],
        'body-lg': ['Hanken Grotesk', 'sans-serif'],
        'body-md': ['Hanken Grotesk', 'sans-serif'],
        'label-md': ['Hanken Grotesk', 'sans-serif'],
        quote: ['Literata', 'serif'],
      },
      fontSize: {
        'display-lg': ['64px', { lineHeight: '1.1', letterSpacing: '-0.02em', fontWeight: '700' }],
        'display-md': ['48px', { lineHeight: '1.2', fontWeight: '600' }],
        'headline-lg': ['32px', { lineHeight: '1.3', fontWeight: '600' }],
        'headline-lg-mobile': ['28px', { lineHeight: '1.3', fontWeight: '600' }],
        'body-lg': ['20px', { lineHeight: '1.6', fontWeight: '400' }],
        'body-md': ['16px', { lineHeight: '1.6', fontWeight: '400' }],
        'label-md': ['14px', { lineHeight: '1.2', letterSpacing: '0.05em', fontWeight: '600' }],
        quote: ['24px', { lineHeight: '1.5', fontWeight: '400' }],
      },
      borderRadius: {
        // rounded-xl = 1.5rem cho card (ghi đè giá trị mặc định của Tailwind)
        xl: '1.5rem',
      },
      spacing: {
        // section-padding: 8rem — giữ cả 2 tên (section / section-padding) để
        // tương thích ngược với các class đã dùng ở Task 1.2 lẫn markup thiết kế gốc.
        section: '8rem',
        'section-padding': '8rem',
        'container-max': '1280px',
        gutter: '2rem',
        'margin-mobile': '1.25rem',
        'stack-sm': '0.5rem',
        'stack-md': '1.5rem',
        'stack-lg': '4rem',
      },
      maxWidth: {
        'container-max': '1280px',
      },
    },
  },
  plugins: [],
};
