import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        name: '',
        path: 'dashboard',
        component: () => import('pages/DashboardPage.vue'),
      },
      {
        name: 'public-courses',
        path: 'public-courses',
        component: () => import('pages/PublicCoursesPage.vue'),
      },
      {
        name: 'create-course',
        path: 'create-course',
        component: () => import('pages/CreateCoursePage.vue'),
      },
      {
        name: 'settings',
        path: 'settings',
        component: () => import('pages/SettingsPage.vue'),
      },
      {
        name: 'profile',
        path: 'profile',
        component: () => import('pages/UserSettingPage.vue'),
      },
      {
        name: 'content',
        path: 'content',
        component: () => import('pages/ContentPage.vue'),
      },
    ],
  },
  {
    path: '/',
    component: () => import('layouts/AuthLayout.vue'),
    children: [
      {
        name: 'register',
        path: 'register',
        component: () => import('pages/RegisterPage.vue'),
      },
      {
        name: 'login',
        path: 'login',
        component: () => import('pages/LoginPage.vue'),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
