<script setup>
import { ref } from 'vue'
import { onKeyStroke } from '@vueuse/core'

const cityName = ref('')
const cityWeatherData = ref('')
const isLoading = ref(false)
const similarCityNames = ref([])
let debounceTimer = null

onKeyStroke('Enter', () => {
  fetchCityWeatherData(cityName)
})

async function delayedCityNamesFetch() {
  clearTimeout(debounceTimer)
  debounceTimer = setTimeout(async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/city-names?city=${cityName.value}`
      );
    if (response.status !== 200) {
      return;
    }
  } catch (error) {
    cityWeatherData.value = error;
  }
  }, 1000);
}

async function fetchCityWeatherData() {
  isLoading.value = true;
  cityWeatherData.value = null;
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/weather/?city=${cityName.value}`
    );
    cityWeatherData.value = await response.json();
    if (response.status !== 200) {
      return;
    }
  } catch (error) {
    cityWeatherData.value = error;
  } finally {
    isLoading.value = false;
  }
}

</script>

<style>
.loading-spinner {
  border: 3.5px solid rgba(0, 0, 0, 0.1);
  border-left-color: #32a164;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
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
  <h2>
    Enter the city name
    <p>
    <input v-model="cityName" id="cityInput" @keyup.enter="fetchCityWeatherData(cityName)">
      <button @click="fetchCityWeatherData(cityName)" :disabled="cityWeatherData == null"> Search</button>
    </p>
    <p v-if="isLoading" class="loading-spinner"></p>
    <pre v-else-if="cityWeatherData">{{ cityWeatherData }}</pre>
    <p v-else></p>
  </h2>
</template>

