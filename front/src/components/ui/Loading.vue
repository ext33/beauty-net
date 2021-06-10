<template>
  <div class="loading container l-container">
    <div class="spin-wrapper">
      <div class="spinner">
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Loading",
  }
</script>

<style scoped>
.spin-wrapper {
  display: flex;
  justify-content: center;
  width: 100%;
}

.spinner {
  height: 60px;
  width: 60px;
  border: 3px solid transparent;
  border-top-color:#5F8CAB;
  border-radius: 50%;
  animation: spin 2s linear infinite;
}

@keyframes spin{
  0% {transform: rotate(0deg);}
  100% {transform: rotate(360deg);}
}
</style>