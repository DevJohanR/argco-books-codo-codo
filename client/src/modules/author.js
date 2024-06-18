import authorService from '../services/authorService';

const state = {
  authors: []
};

const mutations = {
  SET_AUTHORS(state, authors) {
    state.authors = authors;
  }
};

const actions = {
  fetchAuthors({ commit }) {
    authorService.getAllAuthors().then(response => {
      commit('SET_AUTHORS', response.data);
    });
  }
};

const getters = {
  allAuthors: (state) => state.authors
};

export default {
  state,
  mutations,
  actions,
  getters
};
