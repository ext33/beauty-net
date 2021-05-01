<template>
<div id="View-Container" class="l-container container">
  <h1>
    ВАША ЗАПИСЬ №{{id.slice(0,10)}}
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
    <button @click="active=!active" class="btn-cont cancel-btn">
      ОТМЕНИТЬ
    </button>
    <vs-dialog prevent-close v-model="active" :blur=true>
      <div class="modal">
        <h4>
          Вы уверены что хотите удалить запись?
        </h4>
        <router-link :to="'/Signup/'+id+'/Cancel'" class="cancel-btn">ДА</router-link>
      </div>
    </vs-dialog>
  </div>
</div>
</template>

<script>
  export default {
    name: "ViewContainer",
    props: ['id', 'data'],
    data:() => ({
      active: false,
    })
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
  border: none;
}
.modal{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin: 5%;
  color: #F7F7F7;
}
h4{
  padding-bottom: 15px;
}
</style>