import axios from 'axios';

const API_URL = 'http://localhost:5000/api/books';

export default {
  getAllBooks() {
    return axios.get(API_URL);
  },
  getBookById(id) {
    return axios.get(`${API_URL}/${id}`);
  },
  createBook(book) {
    return axios.post(API_URL, book);
  },
  updateBook(id, book) {
    return axios.put(`${API_URL}/${id}`, book);
  },
  deleteBook(id) {
    return axios.delete(`${API_URL}/${id}`);
  }
};
