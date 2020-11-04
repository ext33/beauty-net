<template>
  <div id="app">
    <MainPage/>
  </div>
</template>

<script>
import MainPage from "@/components/pages/main/MainPage";
export default {
  components: {MainPage}
}
</script>

<style>
#app{
  font-family: Montserrat, sans-serif;
}
.container{
  padding-right: 10%;
  padding-left: 10%;
}
body {
  background-color: #1E2327;
  margin: 0;
}
</style>
