<template>
  <div id="view-signup-page">
    <ViewContainer :id="id" :data="data"/>
  </div>
</template>

<script>
import ViewContainer from "@/components/pages/viewsignup/ViewContainer";
import api from "@/axios";
export default {
  name: "ViewSignupPage",
  components: {ViewContainer},
  props: ['id', 'data'],
  beforeMount() {
    let data = api.get_signup(this.$route.params.id)
    if (data===404){
      this.$router.push({path:'/errors'})
    }
    else if (data===500){
      this.$router.push({path:'/Error'})
    }
    else {
      return data
    }
  },
  data:() => {
    
  }
}
</script>

<style scoped>

</style>