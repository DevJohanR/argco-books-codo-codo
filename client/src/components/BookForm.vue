<template>
  <form @submit.prevent="handleSubmit">
    <div>
      <label for="isbn">ISBN</label>
      <input type="text" v-model="book.isbn" id="isbn" required />
    </div>
    <div>
      <label for="title">Title</label>
      <input type="text" v-model="book.title" id="title" required />
    </div>
    <div>
      <label for="cover">Cover</label>
      <input type="text" v-model="book.cover" id="cover" required />
    </div>
    <div>
      <label for="synopsis">Synopsis</label>
      <textarea v-model="book.synopsis" id="synopsis" required></textarea>
    </div>
    <div>
      <label for="publication_date">Publication Date</label>
      <input type="date" v-model="book.publication_date" id="publication_date" required />
    </div>
    <div>
      <label for="author">Author</label>
      <select v-model="book.author_id" id="author" required>
        <option v-for="author in authors" :key="author.id" :value="author.id">
          {{ author.first_name }} {{ author.last_name }}
        </option>
      </select>
    </div>
    <div>
      <label for="category">Category</label>
      <select v-model="book.category_id" id="category" required>
        <option v-for="category in categories" :key="category.id" :value="category.id">
          {{ category.name }}
        </option>
      </select>
    </div>
    <button type="submit">Submit</button>
  </form>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  data() {
    return {
      book: {
        isbn: '',
        title: '',
        cover: '',
        synopsis: '',
        publication_date: '',
        author_id: null,
        category_id: null
      }
    };
  },
  computed: {
    ...mapGetters({
      authors: 'allAuthors',
      categories: 'allCategories'
    })
  },
  methods: {
    ...mapActions(['createBook', 'updateBook', 'fetchAuthors', 'fetchCategories']),
    handleSubmit() {
      if (this.book.id) {
        this.updateBook({ id: this.book.id, book: this.book });
      } else {
        this.createBook(this.book);
      }
      this.$router.push('/');
    }
  },
  created() {
    this.fetchAuthors();
    this.fetchCategories();
  }
};
</script>
