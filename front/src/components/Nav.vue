<template>
  <nav class="container">
    <div class="logo">
      <a href="" class="text-logo">
        <span class="text1">BEAUTY</span><br>
        <span class="text2">NET</span>
      </a>
    </div>
    <vs-button @click="activeSidebar = !activeSidebar" flat icon>
      <font-awesome-icon icon="bars" style="height: 45px; width: 44px; color: #F7F7F7" />
    </vs-button>
    <vs-sidebar
        absolute
        right
        background="primary"
        text-white
        v-model="active"
        :open.sync="activeSidebar"
    >
      <template #logo>
        <!-- ...img logo -->
      </template>
      <vs-sidebar-item id="home">
        <template #icon>
          <i class='bx bx-home'></i>
        </template>
        Главная
      </vs-sidebar-item>
      <vs-sidebar-item id="info">
        <template #icon>
          <i class='bx bx-home'></i>
        </template>
        Услуги
      </vs-sidebar-item>
      <vs-sidebar-item id="signup">
        <template #icon>
          <i class='bx bx-home'></i>
        </template>
        Записаться
      </vs-sidebar-item>
      <vs-sidebar-item id="contacts">
        <template #icon>
          <i class='bx bx-home'></i>
        </template>
        Контакты
      </vs-sidebar-item>
      <vs-sidebar-item id="info">
        <template #icon>
          <i class='bx bx-home'></i>
        </template>
        О нас
      </vs-sidebar-item>
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
  height: 64px;
  display: flex;
  align-items: center;
}
.text-logo{
  margin: 0;
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
.vs-sidebar-content{
  border-radius: 0 !important;
}
</style>