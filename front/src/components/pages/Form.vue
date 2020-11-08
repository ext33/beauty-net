<template>
  <form class="signup-form">
    <label>
      <input type="text" class="input-main" placeholder="ВВЕДИТЕ ВАШЕ ИМЯ" required>
      <input type="tel" class="input-main" placeholder="ВЫБЕРИТЕ УСЛУГУ" required>
      <input type="tel" class="input-main" placeholder="ВЫБЕРИТЕ ДАТУ" required>
      <input type="tel" class="input-main" placeholder="ВЫБЕРИТЕ ВРЕМЯ" required>
      <input type="tel" class="input-main" placeholder="ВЫБЕРИТЕ МАСТЕРА" required>
      <input type="tel" class="input-main" placeholder="ВЫБЕРИТЕ ФИЛИАЛ" required>
      <input type="submit" class="input-main input-submit">
    </label>

  </form>
</template>

<script>
export default {
name: "Form"
}
</script>

<style scoped>
.signup-form{
  display: flex;
  justify-content: center;
  align-items: center;
}
.input-main{
  margin-bottom: 20px;
  padding: 10px 20px;
  width: 60%;
  font-size: 18px;
  border-radius: 10px;
  border: 0;
  color: #7A838B;
}
.input-submit{
  color: #F7F7F7;
  background-color: #5F8CAB;
  width: 66%;
}
</style>