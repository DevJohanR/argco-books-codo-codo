<template>
  <div>
    <h1>Books</h1>
    <ul>
      <li v-for="book in books" :key="book.id">
        <router-link :to="`/books/${book.id}`">{{ book.title }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  computed: {
    ...mapGetters(['allBooks'])
  },
  methods: {
    ...mapActions(['fetchBooks'])
  },
  created() {
    this.fetchBooks();
  }
};
</script>
