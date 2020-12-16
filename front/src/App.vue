<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {

}
</script>

<style>
body{
  background-color: #1E2327;
  margin: 0;
}

#app{
  font-family: Montserrat, sans-serif;
}
.container{
  padding-right: 10%;
  padding-left: 10%;
}
.l-container{
  height: 70vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  color: #F7F7F7;
  text-align: center;
  align-content: center;
}
.m-button{
  border: 0;
  border-radius: 12px;
  padding: 10px 22px;
  font-size: 18px;
  font-weight: bold;
  color: #F7F7F7;
  background-color: #5F8CAB;
  margin-top: 10px;
}
.m-wd-button{
  padding: 10px 40px;
}
.form-area{
  margin-top: 52px;
  height: 70%;
  width: 660px;
  border-radius: 30px;
  background-color: #3E454D;
  padding: 80px 0;
}
a{
  text-decoration: none !important;
  color: #F7F7F7;
}
.vs-input{
  width: 100% !important;
  padding: 10px 20px !important;
}
.vs-select__input {
  padding: 8px 13px !important;
}
</style>
