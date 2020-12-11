<template>
  <div id="cancel-signup-page">
    <CancelResult :id="id"/>
  </div>
</template>

<script>
import CancelResult from "@/components/pages/cancelsignup/CancelResult";
import api from "@/axios";
export default {
  name: "CancelSignupPage",
  components: {CancelResult},
  props: ['id'],
  beforeMount() {
    let check = api.id_check(this.$route.params.id)
    if (check===0){
      this.$router.push({path:'/404'})
    }
  }
}
</script>

<style scoped>
</style>