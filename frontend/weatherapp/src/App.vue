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
  similarCityNames.value = [];
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
      similarCityNames.value.push(cityName['name']);
    });
  }, 250);
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

function fetchSelectedCityWeatherData() {
  fetchCityWeatherData(selectedCity.value)
}
</script>

<style>
* {
  font-family: 'Poppins', sans-serif;
}
.loading-spinner {
  border: 3.5px solid rgba(39, 47, 122, 0.1);
  border-left-color: #32a164;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
}
.search-container {
  position: absolute;
  background-color: #131535;
  /* color: #102818; */
  border-radius: 12px;
  top: 40px;
  /* height: 400px; */
  /* top: 50%; */
  width: 600px;
  border-radius: 25px;

  padding: 20px;
  /* align-items: flex-start; */
  /* max-width: 1000px; */

}

/* .dropdown {
  position: absolute;
  top: 100%;
  width: 100%;
  background-color: #102818;
  max-height: 280px;
  overflow-y: auto;
  border-radius: 12px;
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
  z-index: 1;
} */
.city-list {
  padding-left: 0;
  margin: px;
}
.city-element {
  font-size: 18px;
  list-style-type: none;
  color: rgb(182, 182, 182);
  background-color: #171b57;
  margin: 6px;
  padding-left: 7px;
  padding-top: 4px;
  padding-bottom: 4px;
  border-radius: 10px;
}
.city-element:hover{
  color: aliceblue;
  background-color: #202675;
  cursor: pointer;
}
.city-search {
  text-align: center;
}

/* CSS */
.search-button {
  align-items: center;
  background-image: linear-gradient(144deg,#AF40FF, #5B42F3 50%,#00DDEB);
  border: 0;
  border-radius: 8px;
  box-shadow: rgba(151, 65, 252, 0.2) 0 15px 30px -5px;
  box-sizing: border-box;
  color: #FFFFFF;
  display: flex;
  font-family: Phantomsans, sans-serif;
  font-size: 20px;
  justify-content: center;
  line-height: 1em;
  max-width: 100%;
  min-width: 140px;
  padding: 19px 24px;
  text-decoration: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  white-space: nowrap;
  cursor: pointer;
}

.search-button:active,
.search-button:hover {
  outline: 0;
}

/* .cityNameInput { */
/* } */
@media (min-width: 768px) {
  .search-button {
    font-size: 24px;
    min-width: 196px;
  }
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
  
  <div class="search-container">
    <div class="city-search">
      <h2>
        Enter The City Name
      </h2>
      <input v-model="cityName" id="cityNameInput" @keyup.enter="fetchCityWeatherData(cityName)">
      <button class="search-button" @click="fetchCityWeatherData(cityName)" :disabled="cityWeatherData == null"> Search</button>
    </div>
    <div v-if="similarCityNames.length" class="dropdown">
      <ul class="city-list">
        <li class="city-element" v-for="city in similarCityNames" :key="city" :value="city" @click="fetchSelectedCityWeatherData">{{ city }}</li>
      </ul>
    </div>
  </div>
  <p v-if="isLoading" class="loading-spinner"></p>
  <pre v-else-if="cityWeatherData">{{ cityWeatherData }}</pre>
  <p v-else></p>
    

</template>

