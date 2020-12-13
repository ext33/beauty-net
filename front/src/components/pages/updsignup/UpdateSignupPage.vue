<template>
  <div id="update-signup-page">
    <SignupContainer :title="title" :id="id"/>
  </div>
</template>

<script>
import SignupContainer from "@/components/SignupContainer";
import api from "@/axios";
export default {
name: "UpdateSignupPage",
  props: ['id'],
  components: {SignupContainer},
  data:() => ({
    title: 'ЗАПИСЬ №',
  }),
  beforeMount() {
    let check = api.id_check(this.$route.params.id)
    if (check===0){
      this.$router.push({path:'/errors'})
    }
  }
}
</script>

<style scoped>

</style>