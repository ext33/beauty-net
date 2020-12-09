<template>
  <div id="signup-page">
    <Nav/>
      <SignupContainer/>
    <Footer/>
  </div>
</template>

<script>
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";
import SignupContainer from "@/components/SignupContainer";
export default {
name: "SignupPage",
  components: {SignupContainer, Footer, Nav},
}
</script>

<style scoped>

</style>