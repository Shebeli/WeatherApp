<script setup>
import { ref, watch } from 'vue'

const cityName = ref('Tehran')
const cityWeatherData = ref(null)

async function fetchCityWeatherData() {
  const response = await fetch(
    `http://127.0.0.1:8000/weather/?city=${cityName.value}`
  )
  cityWeatherData.value = await response.json()
}

fetchCityWeatherData()
watch(cityWeatherData, fetchCityWeatherData)

</script>

<template>
  <h2>
    Enter the city name {{ cityName }}
    <p><input v-model="cityName"></p>
    <p>data: {{ cityWeatherData }}</p>
  </h2>
  
      
</template>