<template>
  <div class="services container">
    <h2 class="services-head">УСЛУГИ</h2>
    <div class="categories">
      <Category/>
      <Category/>
      <Category/>
    </div>
    <div class="services-cont">
      <Service/>
      <Service/>
      <Service/>
      <Service/>
    </div>
  </div>
</template>

<script>
import Category from "@/components/pages/main/Category";
import Service from "@/components/pages/main/Service";
export default {
name: "Services",
  components: {Service, Category}
}
</script>

<style scoped>
.services{
  padding: 96px 25%;
  display: flex;
  justify-content: center;
  color: #F7F7F7;
  flex-direction: column;
}
.services-head{
  font-size: 36px;
  text-align: center;
}
.categories{
  padding-top: 20px;
  padding-bottom: 100px;
}
</style>