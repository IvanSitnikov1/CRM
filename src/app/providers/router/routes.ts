export const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/pages/home'),
    meta: { requiresAuth: true }
  },
  {
    path: '/nears-events',
    name: 'vents',
    component: () => import('@/pages/nearest-events'),
    meta: { requiresAuth: true }
  },
  {
    path: '/calendar',
    component: () => import('@/pages/calendar'),
    meta: { requiresAuth: true }
  },
  {
    path: '/projects',
    component: () => import('@/pages/progects'),
    meta: { requiresAuth: true }
  },
  {
    path: '/projects/details',
    component: () => import('@/pages/project-details'),
    meta: { requiresAuth: true }
  },
  {
    path: '/vacations',
    component: () => import('@/pages/vacations'),
    meta: { requiresAuth: true }
  },
  {
    path: '/employees',
    component: () => import('@/pages/employees'),
    meta: { requiresAuth: true }
  },
  {
    path: '/messenger',
    component: () => import('@/pages/messenger'),
    meta: { requiresAuth: true }
  },
  {
    path: '/login',
    component: () => import('@/pages/login')
  },
  {
    path: '/profile',
    component: () => import('@/pages/profile'),
    meta: { requiresAuth: true }
  },
  {
    path: '/:pathMatch(.*)',
    component: () => import('@/pages/not-found'),
    meta: { requiresAuth: true }
  }
];
