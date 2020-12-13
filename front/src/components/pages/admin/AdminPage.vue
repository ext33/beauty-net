<template>
<div>

</div>
</template>

<script>
export default {
name: "AdminPage",
  beforeMount() {
    window.location.href = 'http://127.0.0.1:8000/admin/login/?next=/admin/'
  }
}
</script>

<style scoped>

</style>