<template>
  <div>
    <b-alert variant="success" show>{{ msg }}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['msg'],
};
</script>
