<template>
  <nav class="container">
    <router-link to="/" class="text-logo">
    <div class="logo">
        <span class="text1">BEAUTY</span>
        <span class="text2">NET</span>
    </div>
    </router-link>
    <vs-button @click="activeSidebar = !activeSidebar" flat icon>
      <font-awesome-icon icon="bars" style="height: 45px; width: 44px; color: #F7F7F7" />
    </vs-button>
    <vs-sidebar
        right
        background="primary"
        text-white
        :square=true
        :open.sync="activeSidebar"
    >
      <template #logo>
        <div class="logo">
          <router-link to="/" class="text-logo">
            <span class="text1">BEAUTY</span><br>
            <span class="text2">NET</span>
          </router-link>
        </div>
      </template>
      <router-link to="/">
        <vs-sidebar-item id="home">
          <template #icon>
            <i class='bx bx-home'></i>
          </template>
          Главная
        </vs-sidebar-item>
      </router-link>
      <vs-sidebar-item id="info">
        <template #icon>
          <i class='bx bx-home'></i>
        </template>
        Услуги
      </vs-sidebar-item>
      <router-link to="/Signup">
        <vs-sidebar-item id="signup">
          <template #icon>
            <i class='bx bx-home'></i>
          </template>
          Записаться
        </vs-sidebar-item>
      </router-link>
      <router-link to="/About">
        <vs-sidebar-item id="contacts">
          <template #icon>
            <i class='bx bx-home'></i>
          </template>
          Контакты
        </vs-sidebar-item>
      </router-link>
      <router-link to="/About">
        <vs-sidebar-item id="info">
          <template #icon>
            <i class='bx bx-home'></i>
          </template>
          О нас
        </vs-sidebar-item>
      </router-link>
    </vs-sidebar>
  </nav>
</template>

<script>
  export default {
    name: "Nav",
    data:() => ({
      activeSidebar: false
    })
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
  height: 70px;
  display: flex;
  flex-direction: column;
}

.text-logo{
  margin: 0;
  padding: 0;
  font-style: normal;
  font-size: 32px;
  line-height: 32px;
  color: #F7F7F7;
}

.text1{
  font-weight: bold;
}

.text2{
  font-weight: lighter;
}
</style>