<template>
 <div class="service">
   <p class="desc">Стрижка машинкой</p>
   <p class="price">2000</p>
 </div>
</template>

<script>
export default {
name: "Service"
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