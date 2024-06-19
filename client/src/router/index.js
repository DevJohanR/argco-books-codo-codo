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
    component: BookEdit,
    props: true
  },
  {
    path: '/books/:id',
    name: 'BookDetail',
    component: BookDetail,
    props: true
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
