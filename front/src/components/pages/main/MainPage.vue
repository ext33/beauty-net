<template>
  <div id="main-page">
    <Nav/>
    <div class="background">
      <Promo/>
    </div>
    <Loading v-if="loading"/>
    <Services v-if="data" :data="data"/>
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
  import api from "@/axios";
  import Loading from "@/components/Loading";

  export default {
    name: "MainPage",
    components: {Footer, Nav, Map, Services, Promo, Loading},
    data(){
      return {
        loading: true,
        data: null,
      }
    },
    beforeMount() {
      this.fetchData()
    },
    methods: {
      async fetchData(){
        this.loading = true
        let data = await api.list_services()
        this.data = await api.check_only_error(data, this.$router)
        this.loading = false
      }
    }
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