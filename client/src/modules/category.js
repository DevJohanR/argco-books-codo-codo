import categoryService from '../../services/categoryService';

const state = {
  categories: []
};

const mutations = {
  SET_CATEGORIES(state, categories) {
    state.categories = categories;
  }
};

const actions = {
  fetchCategories({ commit }) {
    categoryService.getAllCategories().then(response => {
      commit('SET_CATEGORIES', response.data);
    });
  }
};

const getters = {
  allCategories: (state) => state.categories
};

export default {
  state,
  mutations,
  actions,
  getters
};
