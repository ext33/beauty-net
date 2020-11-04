<template>
  <div class="main-comp">
    <p class="m-main-text">
      САЛОН КРАСОТЫ <br> BEAUTY NET
    </p>
    <p class="m-second-text">
      для записи выберите ближайший филиал
    </p>
    <button class="m-button">
      записаться
    </button>
  </div>
</template>

<script>
export default {
name: "MainComponent"
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
.m-button{
  border: 0;
  border-radius: 12px;
  padding: 10px 22px;
  font-size: 18px;
  font-weight: bold;
  color: #F7F7F7;
  background-color: #5F8CAB;
}
</style>