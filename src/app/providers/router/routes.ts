import { HomeLayout } from '@/widgets/home-layout/'

export const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/pages/home'),
  },
  {
    path: '/calendar',
    component: () => import('@/pages/calendar'),
  },
  {
    path: '/:pathMatch(.*)',
    component: () => import('@/pages/not-found'),
  }
]
