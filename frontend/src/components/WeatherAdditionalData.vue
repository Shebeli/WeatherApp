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
      <ion-icon id='HumidityIcon' name="water-outline"></ion-icon>
      Humidity: {{ weatherData.cityweather.humidity }}%
    </p>
    <p id="Windspeed" >
      <ion-icon id="WindIcon" name="shuffle-outline"></ion-icon>
      Wind: {{ weatherData.citywind.wind_speed }}m/s
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
}

#Humidity {
  position: absolute;
  bottom: 0%;
  right: 40%;
  font-size: 17px;
}

#HumidityIcon {
  color: #1ca3ec;
}

#Windspeed {
  position:absolute;
  bottom: 0%;
  left: 68%;
  font-size: 17px;
}

#WindIcon {
  color: aquamarine;
}
.weather-additional {
  position: relative;
  min-width: 300px;
  min-height: 35px;
  margin-top: 10px;
  border: 2rem red;
  /* background-color: rgb(44, 44, 44); */
}
</style>