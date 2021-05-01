<template>
  <div class="services container">
    <h2 class="services-head">УСЛУГИ</h2>
    <div class="services-cont" v-if="data.length>0">
      <Service v-for="item in data" :key=item.id :title=item.name :price=item.price />
    </div>
    <div class="services-nf" v-else >
      Сейчас услуг нет...
    </div>
  </div>
</template>

<script>
  import Service from "@/components/pages/main/Service";
  
  export default {
    name: "Services",
    components: {Service},
    props: ['data'],
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
.services-nf{
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 32px;
  margin-top: 70px;
}
</style>