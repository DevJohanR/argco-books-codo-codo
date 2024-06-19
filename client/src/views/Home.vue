<template>
  <div>
    <h1>Library</h1>
    <SearchBar @search="handleSearch" />
    <button @click="navigateToAdd">Add Book</button>
    <BookList :books="filteredBooks" />
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import SearchBar from "../components/SearchBar.vue";
import BookList from "../components/BookList.vue";

export default {
  components: {
    SearchBar,
    BookList
  },
  data() {
    return {
      searchQuery: ""
    };
  },
  computed: {
    ...mapGetters(["allBooks"]),
    filteredBooks() {
      return this.allBooks.filter(book =>
        book.title.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    }
  },
  methods: {
    ...mapActions(["fetchBooks"]),
    handleSearch(query) {
      this.searchQuery = query;
    },
    navigateToAdd() {
      this.$router.push("/books/add");
    }
  },
  created() {
    this.fetchBooks();
  }
};
</script>
