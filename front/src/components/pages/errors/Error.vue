<template>
  <div id="error-page" class="l-container container">
    <h1 class="text-info">
      /error/<br><br> Произошла ошибка. Повторите позже.
    </h1>
    <router-link to="/" class="m-button m-wd-button">
      Вернуться на главную
    </router-link>
  </div>
</template>

<script>
export default {
name: "Error"
}
</script>

<style scoped>

</style>