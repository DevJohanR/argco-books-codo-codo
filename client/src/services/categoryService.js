import axios from 'axios';

const API_URL = 'http://localhost:5000/api/categories';

export default {
  getAllCategories() {
    return axios.get(API_URL);
  },
  getCategoryById(id) {
    return axios.get(`${API_URL}/${id}`);
  }
};
