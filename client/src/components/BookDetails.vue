<template>
  <div v-if="book">
    <h1>{{ book.title }}</h1>
    <p>{{ book.synopsis }}</p>
    <p><strong>Author:</strong> {{ book.author.first_name }} {{ book.author.last_name }}</p>
    <p><strong>Category:</strong> {{ book.category.name }}</p>
    <router-link :to="`/books/${book.id}/edit`">Edit</router-link>
    <button @click="deleteBook(book.id)">Delete</button>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  computed: {
    ...mapGetters(['currentBook'])
  },
  methods: {
    ...mapActions(['fetchBook', 'deleteBook']),
    async deleteBook(id) {
      await this.deleteBook(id);
      this.$router.push('/');
    }
  },
  created() {
    const id = this.$route.params.id;
    this.fetchBook(id);
  }
};
</script>
