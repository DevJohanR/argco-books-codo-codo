import bookService from "../services/bookService";

const state = {
  books: [],
  book: null
};

const mutations = {
  SET_BOOKS(state, books) {
    state.books = books;
  },
  SET_BOOK(state, book) {
    state.book = book;
  }
};

const actions = {
  fetchBooks({ commit }) {
    bookService.getAllBooks().then(response => {
      commit("SET_BOOKS", response.data);
    });
  },
  fetchBook({ commit }, id) {
    bookService.getBookById(id).then(response => {
      commit("SET_BOOK", response.data);
    });
  },
  createBook({ dispatch }, book) {
    bookService.createBook(book).then(() => {
      dispatch("fetchBooks");
    });
  },
  updateBook({ dispatch }, { id, book }) {
    bookService.updateBook(id, book).then(() => {
      dispatch("fetchBooks");
    });
  },
  deleteBook({ dispatch }, id) {
    bookService.deleteBook(id).then(() => {
      dispatch("fetchBooks");
    });
  }
};

const getters = {
  allBooks: state => state.books,
  currentBook: state => state.book
};

export default {
  state,
  mutations,
  actions,
  getters
};
