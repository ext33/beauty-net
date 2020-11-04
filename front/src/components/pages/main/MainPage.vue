<template>
  <div id="main-page">
    <div class="background">
      <Nav/>
      <MainComponent/>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";
import MainComponent from "@/components/pages/main/MainComponent";

export default {
  name: "MainPage",
  components: {MainComponent, Footer, Nav}
}
</script>

<style scoped>
.background{
  height: 100vh;
  width: 100%;
  background: url("../../../images/background.png") no-repeat center;
  background-size: cover;
  padding: 0 !important;
  margin: 0 !important;
}
</style>