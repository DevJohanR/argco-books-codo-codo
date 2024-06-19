<template>
  <div class="search-bar">
    <input
      type="text"
      v-model="query"
      placeholder="Search for books..."
      @input="handleInput"
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: ""
    };
  },
  methods: {
    handleInput() {
      this.$emit("search", this.query);
    }
  }
};
</script>

<style scoped>
.search-bar {
  margin: 1em 0;
}
.search-bar input {
  width: 100%;
  padding: 0.5em;
  font-size: 1em;
  border-radius: 4px;
  border: 1px solid #ccc;
}
</style>
