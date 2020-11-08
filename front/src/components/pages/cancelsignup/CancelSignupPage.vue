<template>
  <div id="cancel-signup-page">
    <Nav/>
    <CancelResult/>
    <Footer/>
  </div>
</template>

<script>
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";
import CancelResult from "@/components/pages/cancelsignup/CancelResult";
export default {
  name: "CancelSignupPage",
  components: {CancelResult, Nav, Footer}

}
</script>

<style scoped>

</style>