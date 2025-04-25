export const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/pages/home'),
    meta: { requiresAuth: false }
  },
  {
    path: '/nears-events',
    component: () => import('@/pages/nearest-events'),
    name: 'nears-events',
    meta: { requiresAuth: false }
  },
  {
    path: '/calendar',
    component: () => import('@/pages/calendar'),
    name: 'calendar',
    meta: { requiresAuth: false }
  },
  {
    path: '/projects',
    component: () => import('@/pages/progects'),
    name: 'projects',
    meta: { requiresAuth: false }
  },
  {
    path: '/projects/details',
    component: () => import('@/pages/project-details'),
    meta: { requiresAuth: false }
  },
  {
    path: '/projects/task',
    component: () => import('@/pages/project-task'),
    meta: { requiresAuth: false }
  },
  {
    path: '/vacations',
    component: () => import('@/pages/vacations'),
    name: 'vacations',
    meta: { requiresAuth: false }
  },
  {
    path: '/employees',
    name: 'employees',
    component: () => import('@/pages/employees'),
    meta: { requiresAuth: false }
  },
  {
    path: '/messenger',
    name: 'messenger',
    component: () => import('@/pages/messenger'),
    meta: { requiresAuth: false }
  },
  {
    path: '/login',
    component: () => import('@/pages/login')
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('@/pages/profile'),
    meta: { requiresAuth: false }
  },
  {
    path: '/my-profile',
    name: 'my-profile',
    component: () => import('@/pages/profile'),
    meta: { requiresAuth: false }
  },
  {
    path: '/:pathMatch(.*)',
    component: () => import('@/pages/not-found'),
    meta: { requiresAuth: false }
  }
];
