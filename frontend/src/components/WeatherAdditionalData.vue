<script setup>
const props = defineProps({
  weatherData: Object
})
</script>

<template>
  <div class="weather-additional">
    <p id="UV">
      <ion-icon id="UVIcon" name="sunny-outline"></ion-icon>
      UV Index: {{ weatherData.cityweather.uv_index }}
    </p>
    <p id="Humidity">
      <ion-icon name="water-outline"></ion-icon>
      Humidity: {{ weatherData.cityweather.humidity }}%
    </p>
    <p id="Windspeed" >
      <ion-icon id="HumidityIcon" name="shuffle-outline"></ion-icon>
      Wind speed: {{ weatherData.citywind.wind_speed }}
    </p>
  </div>
</template>

<style>
#UV {
  position: absolute;
  bottom: 0%;
  font-size: 17px;
}

#UVIcon {
  position: relative;
  color: rgb(125, 35, 125);
  font-size: 17px;
}

#Humidity {
  position: absolute;
  bottom: 0%;
  right: 40%;
  font-size: 17px;
}

#HumidityIcon {
  font-size: 17px;
  color: aquamarine;
}

#Windspeed {
  position:absolute;
  bottom: 0%;
  left: 65%;
}

.weather-additional {
  margin-top: 20px;
  border: 2rem red;
  background-color: rgb(44, 44, 44);
}
</style>