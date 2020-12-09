<template>
  <div id="view-signup-page">
    <Nav/>
    <ViewContainer/>
    <Footer/>
  </div>
</template>

<script>
import Nav from "@/components/Nav";
import Footer from "@/components/Footer";
import ViewContainer from "@/components/pages/viewsignup/ViewContainer";
export default {
  name: "ViewSignupPage",
  components: {ViewContainer, Footer, Nav}
}
</script>

<style scoped>

</style>