<template>
  <div id="main-page">
    <div class="background">
      <Nav/>
      <Promo/>
    </div>
    <Services/>
    <Map/>
    <Footer/>
  </div>
</template>

<script>
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";
import Promo from "@/components/pages/main/Promo";
import Services from "@/components/pages/main/Services";
import Map from "@/components/pages/main/Map";

export default {
  name: "MainPage",
  components: {Map, Services, Promo, Footer, Nav},
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