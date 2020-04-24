<template>
<div
    id="app"
    class="min-h-screen w-screen bg-gray-200 flex flex-col pt-20 \n
    justify-center items-center md:items-start md:flex-row"
  >
    <div class="w-full max-w-md text-center px-3">
      <p class="mb-2 text-gray-700 font-semibold font-sans tracking-wide">Inbox</p>
      <draggable
        group="all-tasks"
        ghost-class="moving-card"
        :list="inbox"
        :animation="200"
      >
        <div v-for="task in inbox"
        :key="task.id"
      class="p-4 mb-3 flex justify-between items-center bg-white shadow rounded-lg cursor-move">
    {{task.assignee}}
    <br>
    {{task.title}}
    </div>
      </draggable>
    </div>

    <div class="w-full max-w-md md:ml-6 text-center px-3">
      <p class="mb-2 text-gray-700 font-semibold font-sans tracking-wide">In Progress</p>
      <draggable
        group="all-tasks"
        ghost-class="moving-card"
        :list="inprogress"
        :animation="200"
      >
        <div v-for="task in inprogress"
        :key="task.id"
      class="p-4 mb-3 flex justify-between items-center bg-white shadow rounded-lg cursor-move">
    {{task.assignee}}
    <br>
    {{task.title}}
    </div>
      </draggable>
    </div>

    <div class="w-full max-w-md md:ml-6 text-center px-3">
      <p class="mb-2 text-gray-700 font-semibold font-sans tracking-wide">Done</p>
      <draggable
        group="all-tasks"
        ghost-class="moving-card"
        :list="done"
        :animation="200"
      >
        <div v-for="task in done"
        :key="task.id"
      class="p-4 mb-3 flex justify-between items-center bg-white shadow rounded-lg cursor-move">
    {{task.assignee}}
    <br>
    {{task.title}}
    </div>
      </draggable>
    </div>

  </div>

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
      inbox: [],
      inprogress: [],
      done: [],
      msg: {},
    };
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.inbox = res.data.inbox;
          this.inprogress = res.data.inprogress;
          this.done = res.data.done;
          this.msg = res.data.msg;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getTasks();
  },
};
</script>
