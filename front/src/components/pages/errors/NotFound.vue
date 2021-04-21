<template>
  <div id="notFound" class="l-container container">
    <h1 class="text-info">
      /404/<br> Такой страницы не существует
    </h1>
    <router-link to="/" class="m-button m-wd-button">
      Вернуться на главную
    </router-link>
  </div>
</template>

<script>
export default {
  name: "NotFound"
}
</script>

<style scoped>
#notFound{
  height: 100vh;
}
</style>