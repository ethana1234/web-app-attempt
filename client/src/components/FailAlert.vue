<template>
  <div>
    <b-alert variant="failure" show dismissible>{{ message }}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message'],
};
</script>
