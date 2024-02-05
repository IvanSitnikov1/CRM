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
    path: '/projects',
    component: () => import('@/pages/progects'),
  },
  {
    path: '/vacations',
    component: () => import('@/pages/vacations'),
  },
  {
    path: '/employees',
    component: () => import('@/pages/employees'),
  },
  {
    path: '/messenger',
    component: () => import('@/pages/messenger'),
  },
  {
    path: '/:pathMatch(.*)',
    component: () => import('@/pages/not-found'),
  }
]
