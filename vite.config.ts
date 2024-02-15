import AutoImport from 'unplugin-auto-import/vite'
import { fileURLToPath, URL } from 'node:url'
import { VitePWA } from 'vite-plugin-pwa'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const manifestForPWA = {
  registerType:'prompt',
  includeAssests:['favicon.ico', "apple-touch-icon.png", "masked-icon.svg"],
  manifest:{
    name:"CRM Software",
    short_name:"CRM",
    description:"I am a simple vite app",
    icons:[{
      src: './android-chrome-192x192.png',
      sizes:'192x192',
      type:'image/png',
      purpose:'favicon'
    },
      {
        src:'./android-chrome-512x512.png',
        sizes:'512x512',
        type:'image/png',
        purpose:'favicon'
      },
      {
        src: './apple-touch-icon.png',
        sizes:'180x180',
        type:'image/png',
        purpose:'apple touch icon',
      },
      {
        src: './maskable_icon.png',
        sizes:'512x512',
        type:'image/png',
        purpose:'any maskable',
      }
    ],
    theme_color:'#3F8CFF',
    background_color:'#F4F9FD',
    display:"standalone",
    scope:'/',
    start_url:"/",
    orientation:'portrait'
  },
};

export default defineConfig({
  plugins: [
    vue(),
    VitePWA(manifestForPWA),
    AutoImport({
      include: [
        /\.[tj]sx?$/, // .ts, .tsx, .js, .jsx
        /\.vue$/,
        /\.vue\?vue/, // .vue
        /\.md$/ // .md
      ],

      // global imports to register
      imports: [
        // presets
        'vue',
        'vue-router',
        // custom
        {
          axios: [
            // default imports
            ['default', 'axios'] // import { default as axios } from 'axios',
          ]
        }
      ]
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
