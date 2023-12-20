<script setup>
import { ref, onMounted } from 'vue'
import { onKeyStroke } from '@vueuse/core'
import weatherConditionIconIds from '@/utils/weatherIcons.js'

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
  const baseFilePath = '/src/assets/static/';
  const weatherIconFileName = weatherConditionIconIds[weatherCode].iconName;
  return baseFilePath + weatherIconFileName
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
    weatherIcon.value = getWeatherIconPath(cityWeatherData.value.cityWeatherCondition.icon)
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
* {
  font-family: 'Inter', sans-serif;
  font-weight: 300;
}
.loading-spinner {
  border: 4.5px solid rgb(85, 143, 4);
  border-left-color: #32a164;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
}
.search-container {
  position: relative;
  background-color: #0f1041;
  border-radius: 12px;
  border: 10px solid #1e065b;
  padding: 20px;
  margin: 10px 10px;
  /* left: 50%; */
  bottom: 10%;
}

.weather-container {
  position: relative;
  background-color: #0f1041;
  border-radius: 12px;
  border: 10px solid #1e065b;
  padding: 20px;
  margin: 10px 10px;
  top: 75%;
}
.city-list {
  padding-left: 0;
  margin-top: 25px;
}
.city-element {
  font-size: 16px;
  list-style-type: none;
  color: rgb(202, 200, 200);
  background-color: #171b57;
  margin: 8px;
  padding-left: 7px;
  padding-top: 2px;
  padding-bottom: 2px;
  border-radius: 10px;
  font-weight: 500;
}
.city-element:hover {
  color: aliceblue;
  background-color: #2f37af;
  cursor: pointer;
  transition: background-color 0.35s ease;
}
.city-search {
  text-align: center;
}

.search-button {
  align-self: right;
  background-image: linear-gradient(144deg, #ae44fa, #6851ff 50%, #0a043c);
  border-radius: 10px;
  box-shadow: rgba(154, 74, 245, 0.2) 0 15px 30px -5px;
  color: #ffffff;
  font-size: 18px;
  justify-content: center;
  padding: 10px 30px;
  cursor: pointer;
  right: 20px;
  top: 60px;
  font-weight: 600;
}

.search-button:hover {
  outline: #000000;
  color: aliceblue;
  background-color: #2f37af;
  cursor: pointer;
  transition: background-color 0.35s ease;
}

#cityNameInput {
  padding: 4px 5px;
  margin: 10px 10px;
  /* border: 3.5px solid #33024a; */
  /* border-radius: 5px; */
  font-size: 20px;
  outline: none;
  border: 2.5px solid #080397;
}

#cityNameInput:focus {
  /* border-color: #0b022f9d; */
  border: 2.5px solid #5f63e8;
}

#cityNameInput::placeholder {
  color: #888787;
  font-weight: 200;
  background-image: url('./assets/static/search_icon.jpg');
  /* background-color: azure; */
  background-size: 27px;
  background-repeat: no-repeat;
  background-position: -4px;
}

#weatherIcon {
  height: 150px;
  width: 150px;
  background-color: none;
  color: none;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
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
    <img :src="weatherIcon" id="weatherIcon" />
    <span>{{ cityWeatherData }}</span>
  </div>
  <p v-else-if="isLoading" class="loading-spinner"></p>

  <p v-else></p>
</template>
