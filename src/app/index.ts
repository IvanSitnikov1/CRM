import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { createHead } from '@unhead/vue'
import VueVirtualScroller from 'vue-virtual-scroller'
import 'vue-virtual-scroller/dist/vue-virtual-scroller.css'

import App from './App.vue'

import { router } from './providers'


export const app = createApp(App).use(createPinia()).use(createHead()).use(router).use(VueVirtualScroller)
