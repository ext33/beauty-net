<template>
 <div id="map">
   <yandex-map :coords="[55.751574, 37.573856]"
               zoom="11"
               style="height: 800px; width: 100%"
               :behaviors="['ruler']"
               :controls="['trafficControl', 'searchControl', 'zoomControl', 'routeButtonControl']"
   >

   </yandex-map>
 </div>
</template>

<script>
import { yandexMap } from 'vue-yandex-maps'

export default {
  name: "Map",
  components: { yandexMap },
}

</script>

<style scoped>
#map{
  padding-top: 100px;
}
</style>