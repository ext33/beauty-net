<template>
  <div id="update-signup-page">
    <SignupContainer :title="title" :id="id"/>
  </div>
</template>

<script>
import SignupContainer from "@/components/SignupContainer";
export default {
name: "UpdateSignupPage",
  props: ['id'],
  components: {SignupContainer},
  data:() => ({
    title: 'ЗАПИСЬ №',
  }),
}
</script>

<style scoped>

</style>