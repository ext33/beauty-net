<template>
  <div class="main-comp container">
    <h1 class="m-main-text">
      САЛОН КРАСОТЫ <br> BEAUTY NET
    </h1>
    <h3 class="m-second-text">
      запишитесь уже сегодня!
    </h3>
    <router-link to="/Signup" class="m-button">
      записаться
    </router-link>
  </div>
</template>

<script>
  export default {
    name: "Promo"
  }
</script>

<style scoped>
.main-comp{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  flex-direction: column;
  color: #F7F7F7;
  height: 100vh;
}

.m-main-text{
  text-align: center;
  font-weight: bold;
  font-size: 36px;
}

.m-second-text{
  font-size: 18px;
  text-align: center;
}
</style>