<template>
  <div class="l-container">
    <div class="info-container">
        <div class="info-about">
            <p class="info-about-count">
                Сеть насчитывыет более 100 филиалов в 40 городах.
            </p>
            <p>
                BEAUTYNET — намного больше, чем просто салон красоты, <br>
                это именно то место, где ты найдёшь себя и свой стиль.
            </p>
        </div>
        <div class="info-contacts">
            <p>
                E-MAIL: BEAUTYNET@YANDEX.RU <br>
                ТЕЛЕФОН: 8 800 000 0000 <br>
                РАБОТАЕМ С 10:00 ДО 22:00
            </p>
        </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "InfoContainer",
  }
</script>

<style scoped>
.info-container{
    border-radius: 30px;
    background-color: #3E454D;
    width: 800px;
    margin-top: 52px;
    padding: 80px 40px;
}

.info-about-count{
    font-size: 24px;
    margin-bottom: 60px;
}

.info-about{
    font-size: 22px;
}

.info-contacts{
    margin-top: 60px;
    font-size: 24px;
}
</style>