<template>
  <div id="cancel-signup-page">
    <Nav/>
    <CancelResult :id="id"/>
    <Footer/>
  </div>
</template>

<script>
  import CancelResult from "@/components/pages/cancelsignup/CancelResult";
  import Nav from "@/components/ui/Nav";
  import Footer from "@/components/ui/Footer";
  
  export default {
    name: "CancelSignupPage",
    components: {Footer, Nav, CancelResult},
    props: ['id'],
  }
</script>

<style scoped>

</style>