<script setup>
import { ref, onMounted, defineAsyncComponent, shallowRef } from 'vue'
import { onKeyStroke } from '@vueuse/core'

import WeatherConditions from './utils/WeatherIcons.vue'
import IconNotFound from './components/icons/IconNotFound.vue'
import WeatherAdditionalData from './components/WeatherAdditionalData.vue'
import PageFooter from './components/PageFooter.vue'

const selectedCityName = ref('')
const cityWeatherData = ref('')
const similarCityNames = ref([])
const weatherIcon = shallowRef('')

const isLoading = ref(false)
const showNotification = ref(false)

let debounceTimer = null

onKeyStroke('Enter', () => {
  fetchCityWeatherData(selectedCityName)
})

function getWeatherIconPath(weatherCode) {
  const weatherIconFile = WeatherConditions[weatherCode].iconFile
  return defineAsyncComponent(weatherIconFile)
}

const closeNotification = () => {
  showNotification.value = false
  localStorage.setItem('notificationClose', 'true')
}

async function fetchSimilarCityNames() {
  clearTimeout(debounceTimer)
  let responseData = []
  similarCityNames.value = []
  debounceTimer = setTimeout(async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/city-names?city=${selectedCityName.value}`
      )
      responseData = await response.json()
      if (response.status !== 200) {
        return
      }
    } catch (error) {
      cityWeatherData.value = error
    }
    similarCityNames.value = []
    responseData.forEach((cityName) => {
      similarCityNames.value.push(cityName['name'])
    })
  }, 600)
}


async function fetchCityWeatherData() {
  isLoading.value = true;
  cityWeatherData.value = null;
  const response = await fetch(
      `http://127.0.0.1:8000/api/current-weather?city=${selectedCityName.value}`
    );
  if (response.status == 200) {   
    cityWeatherData.value = await response.json();  
    const iconFile = getWeatherIconPath(cityWeatherData.value.cityweathercondition.icon);
    weatherIcon.value = iconFile;
  }
  else if (response.status == 404) {
    cityWeatherData.value = 404;
  }
  else {
    console.error(response)
  }
  isLoading.value = false;
  similarCityNames.value = '';
}

onMounted(() => {
  const inputField = document.getElementById('cityNameInput');
  inputField.addEventListener('input', fetchSimilarCityNames);
  if (!localStorage.getItem('notificationClose')) {
    showNotification.value = true;
  }
})

function fetchSelectedCityWeatherData(city) {
  similarCityNames.value = ''
  selectedCityName.value = city
  fetchCityWeatherData()
}
</script>

<style>
@import './main.css';
</style>

<template>
  <div v-if="showNotification" class="overlay"></div>
  <div v-if="showNotification" class="notification">
    <p>Welcome to my first application made with Vue3.</p>
    <p>
      If you have any suggestions or feedback for this app, you can contact me through my socials.
    </p>
    <p>Also if you like this simple app, please consider leaving a star on the github page 😉</p>
    <ion-icon name="close-circle-sharp" @click="closeNotification"></ion-icon>
  </div>
  <div class="main">
    <div class="search-container">
      <div class="city-search">
        <input
          placeholder="    City Name"
          v-model="selectedCityName"
          id="cityNameInput"
          @keyup.enter="fetchCityWeatherData(selectedCityName)"
        />
        <button
          class="search-button"
          @click="fetchCityWeatherData(selectedCityName)"
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
            @click="fetchSelectedCityWeatherData(city)"
          >
            {{ city }}
          </li>
        </ul>
      </div>
    </div>
    <div class="city-not-found" v-if="cityWeatherData == '404'">
      <h2>Given city name was not found!</h2>
      <IconNotFound/>
    </div>
    <div class="weather-container" v-else-if="cityWeatherData">
      <weatherIcon id="weatherIcon" />
      <div class="weather-main">
        <h1>{{ cityWeatherData.name }}</h1>
        <h1>{{ Math.round(cityWeatherData.cityweather.temp) }}°C</h1>
        <p>
          {{ Math.floor(cityWeatherData.cityweather.temp_min) }}°C /
          {{ Math.ceil(cityWeatherData.cityweather.temp_max) }}°C
        </p>
        <p>Feels like: {{ Math.round(cityWeatherData.cityweather.feels_like) }}°C</p>
      </div>
      <WeatherAdditionalData :weatherData="cityWeatherData" />
    </div>
    <p v-else-if="isLoading" class="loading-spinner"></p>
  </div>
  <PageFooter />
</template>
