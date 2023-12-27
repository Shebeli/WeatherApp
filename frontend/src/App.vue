<script setup>
import { ref, onMounted } from 'vue'
import { onKeyStroke } from '@vueuse/core'

import WeatherConditions from './utils/weatherIcons.vue'

const cityName = ref('')
const cityWeatherData = ref('')
const isLoading = ref(false)
const similarCityNames = ref([])
const selectedCity = ref('')
const weatherIcon = ref('')

let debounceTimer = null


onKeyStroke('Enter', () => {
  fetchCityWeatherData(cityName)
})

function getWeatherIconPath(weatherCode) {
  const weatherIconFileName = WeatherConditions[weatherCode].iconFile;
  return weatherIconFileName
}

async function fetchSimilarCityNames() {
  clearTimeout(debounceTimer)
  let responseData = []
  similarCityNames.value = []
  debounceTimer = setTimeout(async () => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/city-names?city=${cityName.value}`)
      responseData = await response.json()
      if (response.status !== 200) {
        return
      }
    } catch (error) {
      cityWeatherData.value = error
    }
    responseData.forEach((cityName) => {
      similarCityNames.value.push(cityName['name'])
    })
  }, 400)
}

async function fetchCityWeatherData() {
  isLoading.value = true
  cityWeatherData.value = null
  try {
    const response = await fetch(`http://127.0.0.1:8000/api/current-weather?city=${cityName.value}`)
    cityWeatherData.value = await response.json()
    if (response.status !== 200) {
      return
    }
  } catch (error) {
    cityWeatherData.value = error
  } finally {
    isLoading.value = false
    weatherIcon.value = getWeatherIconPath(cityWeatherData.value.cityweathercondition.icon)
  }
}

onMounted(() => {
  const inputField = document.getElementById('cityNameInput')
  inputField.addEventListener('input', fetchSimilarCityNames)
})

function fetchSelectedCityWeatherData() {
  fetchCityWeatherData(selectedCity.value)
}
</script>

<style>
  @import './main.css';
</style>

<template>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&family=Poppins:wght@500&display=swap"
    rel="stylesheet"
  />
  <div class="search-container">
    <div class="city-search">
      <input
        placeholder="    City Name"
        v-model="cityName"
        id="cityNameInput"
        @keyup.enter="fetchCityWeatherData(cityName)"
      />
      <button
        class="search-button"
        @click="fetchCityWeatherData(cityName)"
        :disabled="cityWeatherData == null"
      >
        Search
      </button>
    </div>
    <div v-if="similarCityNames.length" class="dropdown">
      <ul class="city-list">
        <li
          class="city-element"
          v-for="city in similarCityNames"
          :key="city"
          :value="city"
          @click="fetchSelectedCityWeatherData"
        >
          {{ city }}
        </li>
      </ul>
    </div>
  </div>
  <div class="weather-container" v-if="cityWeatherData">
    <weatherIcon/>
    <span>{{ cityWeatherData }}</span>
  </div>
  <p v-else-if="isLoading" class="loading-spinner"></p>
</template>
