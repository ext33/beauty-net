<template>
  <div id="signup-page">
    <Nav/>
    <SignupContainer :title="title"/>
  </div>
</template>

<script>
  import SignupContainer from "@/components/SignupContainer";
  import Nav from "@/components/Nav";

  export default {
    name: "SignupPage",
    components: {Nav, SignupContainer},
    data:() => ({
      title: 'ЗАПИСЬ НА УСЛУГУ'
    }),
  }
</script>

<style scoped>

</style>