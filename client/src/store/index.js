import { createStore } from 'vuex';
import book from './modules/book';
import category from './modules/category';
import author from './modules/author';

export default createStore({
  modules: {
    book,
    category,
    author
  }
});
