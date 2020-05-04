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
        :list="INBOX"
        :animation="200">
        <div v-for="task in INBOX"
        :key="task.id"
      class="p-4 mb-3 flex justify-between items-center bg-white shadow rounded-lg cursor-move">
    {{task.assignee}}
    <br>
    {{task.title}}
    <br>
    <button
        type="button"
        class="btn btn-warning btn-sm"
        v-b-modal.task-update-modal
        @click="editTask(task)">
      Update
    </button>
    </div>
      </draggable>
    </div>

    <div class="w-full max-w-md md:ml-6 text-center px-3">
      <p class="mb-2 text-gray-700 font-semibold font-sans tracking-wide">In Progress</p>
      <draggable
        group="all-tasks"
        ghost-class="moving-card"
        :list="INPROGRESS"
        :animation="200">
        <div v-for="task in INPROGRESS"
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
        :list="DONE"
        :animation="200">
        <div v-for="task in DONE"
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
            <b-form-checkbox v-model="addTaskForm.done"
                            id="form-checks" value=true>Done?</b-form-checkbox>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

    <b-modal ref="editTaskModal"
            id="task-update-modal"
            title="Update"
            hide-footer>
    <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
    <b-form-group id="form-title-edit-group"
                  label="Title:"
                  label-for="form-title-edit-input">
        <b-form-input id="form-title-edit-input"
                      type="text"
                      v-model="editForm.title"
                      required
                      placeholder="Enter title">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-assignee-edit-group"
                    label="Assignee:"
                    label-for="form-author-edit-input">
          <b-form-input id="form-assignee-edit-input"
                        type="text"
                        v-model="editForm.assignee"
                        required
                        placeholder="Enter assignee">
          </b-form-input>
        </b-form-group>
      <b-form-group id="form-done-edit-group">
          <b-form-checkbox v-model="editForm.done" id="form-checks"
                          value=true>Done?</b-form-checkbox>
      </b-form-group>
      <b-button-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-button-group>
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
      INBOX: [],
      INPROGRESS: [],
      DONE: [],
      msg: '',
      showMessage: false,
      addTaskForm: {
        title: '',
        assignee: '',
        done: false,
      },
      editForm: {
        id: '',
        title: '',
        assignee: '',
        done: false,
      },
    };
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5000/tasks';
      axios.get(path)
        .then((res) => {
          this.INBOX = res.data.INBOX;
          this.INPROGRESS = res.data.INPROGRESS;
          this.DONE = res.data.DONE;
          // this.msg = res.data.msg;
          // this.msg = 'Message';
        })
        .catch((error) => {
          // eslint-disable-next-line
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
          // eslint-disable-next-line
          console.log(error);
          this.getTasks();
        });
    },
    initForm() {
      this.addTaskForm.title = '';
      this.addTaskForm.assignee = '';
      this.addTaskForm.done = false;
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.assignee = '';
      this.editForm.done = false;
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      let done = false;
      if (this.addTaskForm.done) done = true;
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
    editTask(task) {
      this.editForm = task;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTaskModal.hide();
      let done = false;
      if (this.editForm.done) done = true;
      const payload = {
        title: this.editForm.title,
        assignee: this.editForm.assignee,
        done,
      };
      this.updateTask(payload, this.editForm.id);
    },
    updateTask(payload, taskID) {
      const path = `http://localhost:5000/tasks/${taskID}`;
      axios.put(path, payload)
        .then(() => {
          this.getTasks();
          this.showMessage = true;
          this.msg = 'Task updated!';
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTasks();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editTaskModal.hide();
      this.initForm();
      this.getTasks();
    },
  },
  created() {
    this.getTasks();
  },
};
</script>
