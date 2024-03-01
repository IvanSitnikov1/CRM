import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createHead } from '@unhead/vue'
import { router } from './providers'
import Toast, { PluginOptions, POSITION } from 'vue-toastification'
import VueVirtualScroller from 'vue-virtual-scroller'
import 'vue-virtual-scroller/dist/vue-virtual-scroller.css'
import 'vue-toastification/dist/index.css'

import App from './App.vue'


const options: PluginOptions = {
  position: POSITION.BOTTOM_CENTER,
  maxToasts: 3
};


export const app = createApp(App).use(createPinia()).use(createHead()).use(router).use(VueVirtualScroller).use(Toast, options)
