import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import BookAdd from '../views/BookAdd.vue';
import BookEdit from '../views/BookEdit.vue';
import BookDetail from '../views/BookDetail.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/books/add',
    name: 'BookAdd',
    component: BookAdd
  },
  {
    path: '/books/:id/edit',
    name: 'BookEdit',
    component: BookEdit
  },
  {
    path: '/books/:id',
    name: 'BookDetail',
    component: BookDetail
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
