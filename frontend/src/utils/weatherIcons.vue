<script>
const weatherConditionIconIds = {
  '11d': {
    iconFile: () => import('@/components/icons/weather/IconThunderStorm.vue'),
    weatherTypes: 'Thunderstorm'
  },
  '09d': {
    iconFile: () => import('@/components/icons/weather/IconRain.vue'),
    weatherTypes: 'Drizzle, Rain'
  },
  '010d': {
    iconFile: () => import('@/components/icons/weather/IconFewCloudsRainDay.vue'),
    weatherTypes: "Rain"
  },
  '010n': {
    iconFile: () => import('@/components/icons/weather/IconFewCloudsRainNight.vue'),
    weatherTypes: "Rain"
  },
  '13d': {
    iconFile: () => import('@/components/icons/weather/IconSnow.vue'),
    weatherTypes: 'Snow'
  },
  '50d': {
    iconFile: () => import('@/components/icons/weather/IconWind.vue'),
    weatherTypes: 'Mist, Dust, Haze, Fog, Smoke, Sand, Ash, Squall, Tornado'
  },
  '01d': {
    iconFile: () => import('@/components/icons/weather/IconClearDay.vue'),
    weatherTypes: 'Clear Day'
  },
  '01n': {
    iconFile: () => import('@/components/icons/weather/IconClearNight.vue'),
    weatherTypes: 'Clear Night'
  },
  '02d': {
    iconFile: () => import('@/components/icons/weather/IconFewCloudsDay.vue'),
    weatherTypes: 'Few Clouds Day'
  },
  '02n': {
    iconFile: () => import('@/components/icons/weather/IconFewCloudsNight.vue'),
    weatherTypes: 'Few Clouds Night'
  },
  '03d': {
    iconFile: () => import('@/components/icons/weather/IconCloudy.vue'),
    weatherTypes: 'Cloudy'
  },
  '03n': {
    iconFile: () => import('@/components/icons/weather/IconCloudy.vue'),
    weatherTypes: 'Cloudy'
  },
  '04d': {
    iconFile: () => import('@/components/icons/weather/IconCloudy.vue'),
    weatherTypes: 'Cloudy'
  },
  '04n': {
    iconFile: () => import('@/components/icons/weather/IconCloudy.vue'),
    weatherTypes: 'Cloudy'
  }
}

export default weatherConditionIconIds;
</script>
