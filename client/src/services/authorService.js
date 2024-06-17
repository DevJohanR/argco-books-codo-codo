import axios from 'axios';

const API_URL = 'http://localhost:5000/api/authors';

export default {
  getAllAuthors() {
    return axios.get(API_URL);
  },
  getAuthorById(id) {
    return axios.get(`${API_URL}/${id}`);
  }
};
