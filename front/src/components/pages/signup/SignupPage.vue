<template>
  <div id="signup-page">
    <Nav/>
    <SignupContainer />
  </div>
</template>

<script>
  import SignupContainer from "@/components/pages/signup/SignupContainer";
  import Nav from "@/components/ui/Nav";

  export default {
    name: "SignupPage",
    components: {Nav, SignupContainer},
  }
</script>

<style scoped>

</style>