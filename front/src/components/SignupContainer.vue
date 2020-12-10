<template>
  <div class="l-container container">
    <h1>
      {{title}}{{id}}
    </h1>
    <div class="form-area">
      <form class="signup-form">
          <vs-input placeholder="ВВЕДИТЕ ВАШЕ ИМЯ" v-model="value" class="input-main"/>
          <vs-select placeholder="ВЫБЕРИТЕ УСЛУГУ" v-model="value" class="input-main">
            <vs-option label="Vuesax" value="1">
              Vuesax
            </vs-option>
          </vs-select>
        <vs-select placeholder="ВЫБЕРИТЕ МАСТЕРА" v-model="value" class="input-main">
          <vs-option label="Vuesax" value="1">
            Vuesax
          </vs-option>
        </vs-select>
        <vs-select placeholder="ВЫБЕРИТЕ ДАТУ" v-model="value" class="input-main">
          <vs-option label="Vuesax" value="1">
            Vuesax
          </vs-option>
        </vs-select>
        <vs-select placeholder="ВЫБЕРИТЕ ВРЕМЯ" v-model="value" class="input-main">
          <vs-option label="Vuesax" value="1">
            Vuesax
          </vs-option>
        </vs-select>
        <vs-select placeholder="ВЫБЕРИТЕ ФИЛИАЛ" v-model="value" class="input-main">
          <vs-option label="Vuesax" value="1">
            Vuesax
          </vs-option>
        </vs-select>
        <input type="submit" class="input-main input-submit">
      </form>
    </div>
  </div>
</template>

<script>
export default {
  props: ['title', 'id'],
  name: "SignupContainer",
  data:() => ({
    value: '',
  }),

}
</script>

<style scoped>
.signup-form{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  flex-direction: column;
}
.input-main{
  padding: 10px 0;
  width: 60%;
  font-size: 18px;
  border-radius: 10px;
  border: 0;
  color: #7A838B;
}
.input-submit{
  color: #F7F7F7;
  background-color: #5F8CAB;
  width: 60%;
  margin-top: 20px;
}
h1{
  padding-top: 30px;
}
.vs-select-content {
  max-width: 100% !important;
}

</style>