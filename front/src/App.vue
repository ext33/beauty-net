<template>
  <div id="app">
    <SignupPage/>
  </div>
</template>

<script>
// import MainPage from "@/components/pages/main/MainPage";
import SignupPage from "@/components/pages/signup/SignupPage";
export default {
  components: {SignupPage}
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
.signup-container{
  height: 70vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  color: #F7F7F7;
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
</style>
