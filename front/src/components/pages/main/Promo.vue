<template>
  <div class="main-comp container">
    <h1 class="m-main-text">
      САЛОН КРАСОТЫ <br> BEAUTY NET
    </h1>
    <h3 class="m-second-text">
      для записи выберите ближайший филиал
    </h3>
    <button class="m-button">
      записаться
    </button>
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
  height: calc(100vh - 18vh);
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