<template>
  <div>
    <h1>Edit Book</h1>
    <BookForm :book="book" />
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import BookForm from '../components/BookForm.vue';

export default {
  components: {
    BookForm
  },
  data() {
    return {
      book: null
    };
  },
  computed: {
    ...mapGetters(['currentBook'])
  },
  methods: {
    ...mapActions(['fetchBook']),
  },
  created() {
    const id = this.$route.params.id;
    this.fetchBook(id).then(() => {
      this.book = this.currentBook;
    });
  }
};
</script>
