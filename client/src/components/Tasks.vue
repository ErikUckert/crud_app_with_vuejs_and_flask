<template>
<div class="content-container">
  <alert :msg="msg" v-if="showMessage"></alert>
  <button type="button" class="btn btn-success btn-sm" v-b-modal.task-modal>Add Task</button>
<div id="app"
    class="min-h-screen w-screen bg-gray-200 flex flex-col pt-20 \n
    justify-center items-center md:items-start md:flex-row">
    <div class="w-full max-w-md text-center px-3">
      <p class="mb-2 text-gray-700 font-semibold font-sans tracking-wide">Inbox</p>
      <draggable
        group="all-tasks"
        ghost-class="moving-card"
        :list="inbox"
        :animation="200">
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
        :animation="200">
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
        :animation="200">
        <div v-for="task in done"
        :key="task.id"
      class="p-4 mb-3 flex justify-between items-center bg-white shadow rounded-lg cursor-move">
    {{task.assignee}}
    <br>
    {{task.title}}
    </div>
      </draggable>
    </div>
    <b-modal ref="addTaskModal"
            id="task-modal"
            title="Add a new task"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addTaskForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-assignee-group"
                      label="Assignee:"
                      label-for="form-assignee-input">
            <b-form-input id="form-assignee-input"
                          type="text"
                          v-model="addTaskForm.assignee"
                          required
                          placeholder="Enter assignee">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-done-group">
          <b-form-checkbox-group v-model="addTaskForm.done" id="form-checks">
            <b-form-checkbox value="true">Done?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

  </div>
  </div>

</template>

<script>
import axios from 'axios';
import Draggable from 'vuedraggable';
import Alert from './Alert.vue';

export default {
  components: {
  // other components
    Draggable,
    alert: Alert,
  },
  data() {
    return {
      inbox: [],
      inprogress: [],
      done: [],
      msg: '',
      showMessage: false,
      addTaskForm: {
        title: '',
        assignee: '',
        done: [],
      },
    };
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5000/tasks';
      axios.get(path)
        .then((res) => {
          this.inbox = res.data.inbox;
          this.inprogress = res.data.inprogress;
          this.done = res.data.done;
          // this.msg = res.data.msg;
          // this.msg = 'Message';
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addTask(payload) {
      const path = 'http://localhost:5000/tasks';
      axios.post(path, payload)
        .then((res) => {
          this.getTasks();
          // this.msg = 'Message';
          this.showMessage = true;
          this.msg = res.data.msg;
        })
        .catch((error) => {
          console.log(error);
          this.getTasks();
        });
    },
    initForm() {
      this.addTaskForm.title = '';
      this.addTaskForm.assignee = '';
      this.addTaskForm.done = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      let done = false;
      if (this.addTaskForm.done[0]) done = true;
      const payload = {
        title: this.addTaskForm.title,
        assignee: this.addTaskForm.assignee,
        done, // property shorthand
      };
      this.addTask(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getTasks();
  },
};
</script>
