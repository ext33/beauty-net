<template>
  <div id="signup-page">
    <Nav/>
    <SignupContainer :title="title"/>
    <Footer/>
  </div>
</template>

<script>
import SignupContainer from "@/components/SignupContainer";
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";
export default {
name: "SignupPage",
  components: {Footer, Nav, SignupContainer},
  data:() => ({
    title: 'ЗАПИСЬ НА УСЛУГУ'
  }),
}
</script>

<style scoped>

</style>