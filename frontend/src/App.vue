<script setup>
import { ref, onMounted, defineAsyncComponent, shallowRef } from 'vue'
import { onKeyStroke } from '@vueuse/core'

import WeatherConditions from './utils/WeatherIcons.vue'
import WeatherAdditionalData from './components/WeatherAdditionalData.vue';


const cityName = ref('')
const cityWeatherData = ref('')
const similarCityNames = ref([])
const selectedCity = ref('')
const weatherIcon = shallowRef('')

const isLoading = ref(false)
const showNotification = ref(false)

let debounceTimer = null

onKeyStroke('Enter', () => {
  fetchCityWeatherData(cityName)
})

function getWeatherIconPath(weatherCode) {
  const weatherIconFile = WeatherConditions[weatherCode].iconFile
  return defineAsyncComponent(weatherIconFile)
}

const closeNotification = () => {
  showNotification.value = false;
  localStorage.setItem('notificationClose', 'true');
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
    const iconFile = getWeatherIconPath(cityWeatherData.value.cityweathercondition.icon)
    weatherIcon.value = iconFile
  }
}

onMounted(() => {
  const inputField = document.getElementById('cityNameInput')
  inputField.addEventListener('input', fetchSimilarCityNames)
  if (!localStorage.getItem('notificationClose')) {
    showNotification.value = true
  }
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
  <div v-if="showNotification" class="overlay"></div>
  <div v-if="showNotification" class="notification">
    <p>
      Welcome to my first application made with Vue3.  
    </p> 
    <p>If you have any suggestions or feedback for this app, you can contact me through my socials.</p>
    <p>Also if you like this simple app, please consider leaving a star on the github page 😉</p>
    <ion-icon name="close-circle-sharp" @click="closeNotification"></ion-icon>
  </div>
  <div class="main">
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
      <weatherIcon id="weatherIcon"/>
      <div class="weather-main">
        <h1>{{ cityWeatherData.name }}</h1>
        <h1>{{ Math.round(cityWeatherData.cityweather.temp) }}°C</h1>
        <p>
          {{ Math.floor(cityWeatherData.cityweather.temp_min) }}°C /
          {{ Math.ceil(cityWeatherData.cityweather.temp_max) }}°C
        </p>
        <p>Feels like: {{ Math.round(cityWeatherData.cityweather.feels_like) }}°C</p>
      </div>
      <WeatherAdditionalData :weatherData="cityWeatherData"/>
    </div>
    <p v-else-if="isLoading" class="loading-spinner"></p>
  </div>
  <footer>
      <h3>Made by Shebeli</h3>
      <h2>
        Made with:
      </h2>
      <span>
        <ion-icon name="logo-python"></ion-icon>
        <ion-icon name="logo-vue"></ion-icon>
        <ion-icon name="logo-css3"></ion-icon>
      </span>
    </footer>
</template>
