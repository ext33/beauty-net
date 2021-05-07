<template>
  <footer class="container">
    <div class="left-text">
      <a>BEAUTYNET@YANDEX.RU</a>
      <p class="time">С 10:00 ДО 22:00</p>
    </div>
    <div class="right-text">
      <router-link to="/About">
        <a href="" class="link">О НАС</a>
      </router-link>
      <router-link to="/">
        <a href="" class="link">УСЛУГИ</a>
      </router-link>
      <router-link to="/About">
        <a href="" class="link">КОНТАКТЫ</a>
      </router-link>
    </div>
  </footer>
</template>

<script>
  export default {
    name: "Footer"
  }
</script>

<style scoped>
footer{
  color: #F7F7F7;
  font-weight: lighter;
  font-size: 18px;
  padding-top: 60px;
  padding-bottom: 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 90px;
  flex-wrap: wrap;
  text-align: center;
}
.left-text{
  height: 40px;
}
.time{
  line-height: 0
}
.right-text{
  display: flex;
  justify-content: right;
}
.link{
  margin-left: 20px;
  color: #F7F7F7;
}
</style>