<template>
  <div id="view-signup-page">
    <ViewContainer :id="id"/>
  </div>
</template>

<script>
import ViewContainer from "@/components/pages/viewsignup/ViewContainer";
export default {
  name: "ViewSignupPage",
  components: {ViewContainer},
  props: ['id'],
}
</script>

<style scoped>

</style>