<template>
  <div id="update-signup-page">
    <Nav/>
    <SignupContainer :title="title" :id="id"/>
    <Footer/>
  </div>
</template>

<script>
import SignupContainer from "@/components/SignupContainer";
import api from "@/axios";
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";
export default {
name: "UpdateSignupPage",
  props: ['id'],
  components: {Footer, Nav, SignupContainer},
  data:() => ({
    title: 'ЗАПИСЬ №',
  }),
  beforeMount() {
    let check = api.id_check(this.$route.params.id)
    if (check===0){
      this.$router.push({path:'/errors'})
    }
  }
}
</script>

<style scoped>

</style>