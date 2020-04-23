<template>
<ul class="w-full max-w-md">
  <draggable ghost-class="moving-card" filter=".action-button" :list="users" :animation="200">
  <li v-for="book in books"
      :key="book.title"
      class="p-4 mb-3 flex justify-between items-center bg-white shadow rounded-lg cursor-move">
    {{book.author}}
  </li>
  </draggable>
</ul>
</template>

<script>
import axios from 'axios';

import Draggable from 'vuedraggable';

export default {
  components: {
  // other components
    Draggable,
  },
  data() {
    return {
      books: [],
      msg: {},
    };
  },
  methods: {
    getBooks() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
          this.msg = res.data.msg;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
