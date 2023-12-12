<script setup>
import { ref, onMounted } from 'vue'
import { onKeyStroke } from '@vueuse/core'

const cityName = ref('')
const cityWeatherData = ref('')
const isLoading = ref(false)
const similarCityNames = ref([])
const selectedCity = ref('')
let debounceTimer = null

onKeyStroke('Enter', () => {
  fetchCityWeatherData(cityName)
})

async function fetchSimilarCityNames() {
  clearTimeout(debounceTimer);
  let responseData = [];
  debounceTimer = setTimeout(async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/city-names?city=${cityName.value}`
      );
      responseData = await response.json();
      if (response.status !== 200) {
        return;
      };
    } 
    catch (error) {
      cityWeatherData.value = error;
    };
    responseData.forEach(cityName => {
      similarCityNames.value.push(cityName[0]);
    });
  }, 1000);
}

async function fetchCityWeatherData() {
  isLoading.value = true;
  cityWeatherData.value = null;
  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/current-weather?city=${cityName.value}`
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


onMounted(() => {
  const inputField = document.getElementById("cityNameInput")
  inputField.addEventListener('input', fetchSimilarCityNames)
})

function onCitySelect() {
  fetchCityWeatherData(selectedCity.value)
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
.search-container {
  position: relative;
}

.dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  background-color: #fff;
  border: 1px solid #ccc;
  max-height: 150px;
  overflow-y: auto;
  z-index: 1;
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
    <div class="search-container">  
      <input v-model="cityName" id="cityNameInput" @keyup.enter="fetchCityWeatherData(cityName)">
      <button @click="fetchCityWeatherData(cityName)" :disabled="cityWeatherData == null"> Search</button>
      <div v-if="similarCityNames.length" class="dropdown">
        <select v-model="selectedCity" @change="onCitySelect">
          <option v-for="city in similarCityNames" :key="city" :value="city">{{ city }}</option>
        </select>
      </div>
    
    </div>
    <p v-if="isLoading" class="loading-spinner"></p>
    <pre v-else-if="cityWeatherData">{{ cityWeatherData }}</pre>
    <p v-else></p>
    
  </h2>
</template>

