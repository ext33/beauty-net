<template>
 <div class="service">
   <p class="desc">{{ title }}</p>
   <p class="price">{{ price }}</p>
 </div>
</template>

<script>
  export default {
    name: "Service",
    props: ['title', 'price']
  }
</script>

<style scoped>
.service{
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  padding-top: 5px;
  padding-bottom: 5px;
  font-size: 18px;
}
.price{
  color: #5F8CAB;
}
</style>