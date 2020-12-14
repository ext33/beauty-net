<template>
<div id="View-Container" class="l-container container">
  <h1>
    ВАША ЗАПИСЬ №{{id}}
  </h1>
  <div class="form-area">
    <div class="info-cont">
      <div class="left-cont">
        <div class="title">ВАШЕ ИМЯ</div>
        <div class="title">УСЛУГА</div>
        <div class="title">ДАТА</div>
        <div class="title">МАСТЕР</div>
        <div class="title">ФИЛИАЛ</div>
      </div>
      <div class="right-cont">
        <div class="view-text" id="name">{{data.FIO}}</div>
        <hr>
        <div class="view-text" id="service">{{data.service}}</div>
        <hr>
        <div class="view-text" id="date">{{data.time}}</div>
        <hr>
        <div class="view-text" id="master">{{data.master}}</div>
        <hr>
        <div class="view-text" id="office">{{data.branch_office}}</div>
        <hr>
      </div>
    </div>
    <div class="btn-cont">
      <router-link :to="'/Signup/'+id+'/Cancel'" class="cancel-btn">ОТМЕНИТЬ</router-link>
    </div>
  </div>
</div>
</template>

<script>
export default {
name: "ViewContainer",
  props: ['id', 'data'],
}
</script>

<style scoped>
.form-area{
  font-size: 26px;
}
h1{
  padding-top: 20px;
}
.info-cont{
  display: flex;
  justify-content: center;
  align-items: center;
}
.left-cont{
  float: left;
  margin-left: 10px;
  text-align: right;
  width: 35%;
}
.right-cont{
  float: right;
  margin-left: 10px;
  text-align: left;
  width: 60%;
}
.title{
  padding: 15px;
}
.view-text{
  padding: 14px;
  min-height: 28px;
}
hr{
  margin: 0;
  width: 80%;
}
.btn-cont{
  margin-top: 60px;
}
.cancel-btn{
  border-radius: 20px;
  background-color: #CE4646;
  padding: 15px 15%;
  text-decoration: none;
  color: #F7F7F7;
  font-size: 18px;
}
</style>