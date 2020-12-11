<template>
  <div id="result">
     <div class="l-container container" id="success" style="display: none">
        <h1 class="text-info">
          Ваша запись успешно отменена!
        </h1>
        <router-link to="/" class="m-button m-wd-button">
          Вернуться на главную
        </router-link>
     </div>
    <div class="l-container container" id="error" style="display: none">
      <h1 class="text-info">
        Произошла ошибка, повторите попытку
      </h1>
      <router-link to="/" class="m-button m-wd-button">
        Вернуться на главную
      </router-link>
      <router-link :to="'/Signup/'+id" class="m-button m-wd-button">
        Вернуться к записи
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "CancelResult",
  props: ['id'],
  methods:{
    load(id){
      let check = 0
      if(id !== undefined){
        // server check
        check = 1
      }
      let style = document.createElement('style');
      if(check===1){
        style.innerHTML = `
          #success {
          display: flex !important;
          }
          `;
        document.head.appendChild(style);
      }
      else {
        style.innerHTML = `
          #error {
          display: flex !important;
          }
          `;
        document.head.appendChild(style);
      }
    }
  },
  beforeMount() {
    this.load(this.$route.params.id)
  }
}
</script>

<style scoped>

</style>