<template>
  <div id="view-signup-page">
    <Nav/>
    <Loading v-if="loading"/>
    <ViewContainer v-if="data" :id="id" :data="data"/>
    <Footer/>
  </div>
</template>

<script>
import ViewContainer from "@/components/pages/viewsignup/ViewContainer";
import api from "@/axios";
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";
import Loading from "@/components/Loading";
export default {
  name: "ViewSignupPage",
  components: {Footer, Nav, ViewContainer, Loading},
  props: ['id'],
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
    async fetchData() {
      this.loading = true
      let data = await api.get_signup(this.$route.params.id)
      this.data = await api.check_error_404(data, this.$router)
      this.loading = false
    }
  }
}
</script>

<style scoped>

</style>