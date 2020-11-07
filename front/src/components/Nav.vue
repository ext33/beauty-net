<template>
  <nav class="container">
    <div class="logo">
      <p class="text-logo">
        <span class="text1">BEAUTY</span><br>
        <span class="text2">NET</span>
      </p>
    </div>
    <button class="menu">
      <font-awesome-icon icon="bars" style="height: 45px; width: 44px; color: #F7F7F7" />
    </button>
  </nav>
</template>

<script>
export default {
name: "Nav"
}
</script>

<style scoped>
nav{
  padding-top: 46px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #F7F7F7;
}
.logo{
  width: 162px;
  height: 64px;
  display: flex;
  align-items: center;
}
.text-logo{
  margin: 0;
  font-style: normal;
  font-size: 32px;
  line-height: 32px;
}
.text1{
  font-weight: bold;
}
.text2{
  font-weight: lighter;
}
.menu{
  width: 45px;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: 0;
  text-decoration: none;
}

</style>