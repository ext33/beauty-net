<template>
  <div id="view-signup-page">
    <ViewContainer :id="id"/>
  </div>
</template>

<script>
import ViewContainer from "@/components/pages/viewsignup/ViewContainer";
import api from "@/axios";
export default {
  name: "ViewSignupPage",
  components: {ViewContainer},
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