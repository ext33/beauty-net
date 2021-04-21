<template>
  <div id="update-signup-page">
    <Nav/>
    <SignupContainer :title="title" :id="id"/>
  </div>
</template>

<script>
import SignupContainer from "@/components/SignupContainer";
import Nav from "@/components/Nav";
export default {
name: "UpdateSignupPage",
  props: ['id'],
  components: {Nav, SignupContainer},
  data:() => ({
    title: 'ЗАПИСЬ №',
  }),

}
</script>

<style scoped>

</style>