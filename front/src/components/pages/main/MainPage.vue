<template>
  <div id="main-page">
    <Nav/>
    <Footer/>
  </div>
</template>

<script>
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";

export default {
  name: "MainPage",
  components: {Footer, Nav}
}
</script>

<style scoped>

</style>