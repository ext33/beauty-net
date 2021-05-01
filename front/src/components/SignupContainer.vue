<template>
  <div class="l-container container">
    <h1>
      {{title}}{{id}}
    </h1>
    <div v-if="offices_data" class="form-area">
      <form class="signup-form">
        <vs-input placeholder="ВВЕДИТЕ ВАШЕ ИМЯ" v-model="name" class="input-main"/>
        <vs-input placeholder="ВВЕДИТЕ ВАШ EMAIL" v-model="email" class="input-main"/>
        <vs-select placeholder="ВЫБЕРИТЕ ФИЛИАЛ" v-model="office" class="input-main" :disabled="offices_disabled" v-on:change="getPersonal(office)">
          <vs-option v-for="item in offices_data" :label=item.address :key="item.id" :value="item.id">
            {{ item.address }}
          </vs-option>
        </vs-select>
        <vs-select placeholder="ВЫБЕРИТЕ МАСТЕРА" v-model="master" class="input-main" :disabled="personal_disabled" v-on:change="getTimes(master); getServices(master)" v-if="renderComponent">
          <vs-option v-for="item in personal_data" :label=item.FIO :key=item.id :value=item.id>
            {{ item.FIO }}
          </vs-option>
        </vs-select>
        <vs-select placeholder="ВЫБЕРИТЕ УСЛУГУ" v-model="service" class="input-main" :disabled="services_disabled" v-if="renderComponent">
          <vs-option v-for="item in services_data" :label=item.name :key=item.id :value=item.id>
            {{ item.name }}
          </vs-option>
        </vs-select>
        <vs-select placeholder="ВЫБЕРИТЕ ВРЕМЯ" v-model="datetime" class="input-main" :disabled="times_disabled" v-if="renderComponent">
          <vs-option v-for="item in signup_times" :label=item.time :key=item.id :value=item.id>
            {{ item.time }}
          </vs-option>
        </vs-select>
        <button v-on:click="setSignup($event)" class="input-main input-submit">Отправить</button>
        <div v-if=error class="error">
          {{ error }}
        </div>
      </form>
    </div>
    <Loading v-if="loading"/>
  </div>
</template>

<script>
  import api from "@/axios";
  import Loading from "@/components/Loading";

  export default {
    props: ['title', 'id'],
    name: "SignupContainer",
    components: {Loading},
    data:() => ({
      name: '',
      email: '',
      service: '',
      master: '',
      datetime: '',
      office: '',
      loading: true,
      services_data: null,
      personal_data: null,
      offices_data: null,
      signup_times: null,
      times_disabled: true,
      offices_disabled: true,
      personal_disabled: true,
      services_disabled: true,
      error: null,
      renderComponent: true,
    }),
    beforeMount() {
      this.fetchData()
    },
    methods: {
      forceRerender () {
        this.renderComponent = false;
        this. $nextTick (() => {
          this.renderComponent = true;
        });
      },

      async fetchData() {
        this.loading = true
        let offices_data = await api.list_offices()
        this.offices_data = await api.check_only_error(offices_data, this.$router)
        if (this.offices_data.length > 0) this.offices_disabled = false
        this.loading = false
      },

      async getTimes(master) {
        let signup_times = await api.list_times(master)
        this.signup_times = await api.check_only_error(signup_times, this.$router)
        this.times_disabled = false
        this.forceRerender()
      },

      async getServices(master) {
        let services_data = await api.services_master(master)
        this.services_data = await api.check_only_error(services_data, this.$router)
        this.services_disabled = false
        this.forceRerender()
      },

      async getPersonal(office) {
        let personal_data = await api.list_personal(office)
        this.personal_data = await api.check_only_error(personal_data, this.$router)
        this.personal_disabled = false
        this.forceRerender()
      },

      async setSignup(event) {
        if (event) {
          event.preventDefault()
        }
        if(this.name && this.email && this.service && this.office && this.master && this.datetime) {
          const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          if (re.test(String(this.email).toLowerCase())){
            this.error = null
            let request = await api.set_signup(this.name,this.email,this.service,this.master,this.datetime,this.office)
            if (request === 404) {
              await this.$router.push({path: '/error'})
            } else if (request === 500) {
              await this.router.push({path: '/error'})
            } else {
              await this.$router.push({path: '/Signup/'+request.id})
            }
          } else {
            this.error = 'Введите корректный email'
          }
        }
        else {
          this.error = 'Заполните все поля'
        }
      }
    }
  }
</script>

<style scoped>
.signup-form{
  padding-top: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  flex-direction: column;
}
.input-main{
  padding: 10px 0;
  width: 65%;
  font-size: 18px;
  border-radius: 10px;
  border: 0;
  color: #7A838B;
}
.input-submit{
  color: #F7F7F7;
  background-color: #5F8CAB;
  margin-top: 20px;
}
h1{
  padding-top: 30px;
}
.vs-select-content {
  max-width: 100% !important;
}
.error{
  display: flex;
  justify-content: center;
  align-items: center;
  color: #CE4646;
  font-weight: bold;
  font-size: 16px;
  padding: 20px;
}
</style>