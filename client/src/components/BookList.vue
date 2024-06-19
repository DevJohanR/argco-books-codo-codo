<template>
  <div>
    <ul class="book-list">
      <li v-for="book in books" :key="book.id" class="book-item">
        <router-link :to="`/books/${book.id}`">{{ book.title }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    books: Array
  }
};
</script>

<style scoped>
.book-list {
  list-style: none;
  padding: 0;
}
.book-item {
  margin: 1em 0;
}
</style>
