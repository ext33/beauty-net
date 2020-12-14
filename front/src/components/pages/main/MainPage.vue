<template>
  <div id="main-page">
    <Nav/>
    <div class="background">
      <Promo/>
    </div>
    <Services/>
    <Map/>
    <Footer/>
  </div>
</template>

<script>
import Promo from "@/components/pages/main/Promo";
import Services from "@/components/pages/main/Services";
import Map from "@/components/pages/main/Map";
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";

export default {
  name: "MainPage",
  components: {Footer, Nav, Map, Services, Promo},
}
</script>

<style scoped>
.background{
  height: 100vh;
  width: 100%;
  background: url("../../../images/background.png") no-repeat center;
  background-size: cover;
  padding: 0 !important;
  margin-top: -120px !important;
}
</style>