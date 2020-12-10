<template>
  <div id="signup-page">
      <SignupContainer :title="title"/>
  </div>
</template>

<script>
import SignupContainer from "@/components/SignupContainer";
export default {
name: "SignupPage",
  components: {SignupContainer},
  data:() => ({
    title: 'ЗАПИСЬ НА УСЛУГУ'
  }),
}
</script>

<style scoped>

</style>