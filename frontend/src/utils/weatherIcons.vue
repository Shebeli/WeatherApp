<script>
import IconCloudy from '@/components/icons/weather/IconCloudy.vue';
import IconParttialyCloudyDay from '@/components/icons/weather/IconParttialyCloudyDay.vue'
import IconParttialyCloudyNight from '@/components/icons/weather/IconParttialyCloudyNight.vue'
import IconClearDay from '@/components/icons/weather/IconClearDay.vue'
import IconClearNight from '@/components/icons/weather/IconClearNight.vue'
// import IconDrizzle from './components/icons/weather/IconDrizzle.vue'
import IconSnowy from '@/components/icons/weather/IconSnowy.vue'
import IconThunderStorm from '@/components/icons/weather/IconThunderStorm.vue'
import IconRain from '@/components/icons/weather/IconRain.vue'
import IconWindy from '@/components/icons/weather/IconWindy.vue'

// needs to be refactored into only import if the icon weather component is requested.
const weatherConditionIconIds = {
    '11d': {
      iconFile: IconThunderStorm,
      weatherTypes: 'Thunderstorm'
    },
    '09d': {
      iconFile: IconRain,
      weatherTypes: 'Drizzle, Rain'
    },
    '13d': {
      iconFile: IconSnowy,
      weatherTypes: 'Snow'
    },
    '50d': {
      iconFile: IconWindy,
      weatherTypes: 'Mist, Dust, Haze, Fog, Smoke, Sand, Ash, Squall, Tornado'
    },
    '01d': {
      iconFile: IconClearDay,
      weatherTypes: 'Clear Day'
    },
    '01n': {
      iconFile: IconClearNight,
      weatherTypes: 'Clear Night'
    },
    '02d': {
      iconFile: IconParttialyCloudyDay,
      weatherTypes: 'Partial Clouds Day'
    },
    '02n': {
      iconFile: IconParttialyCloudyNight,
      weatherTypes: 'Partial Clouds Night'
    },
    '03d': {
      iconFile: IconCloudy,
      weatherTypes: 'Cloudy'
    },
    '03n': {
      iconFile: IconCloudy,
      weatherTypes: 'Cloudy'
    },
    '04d': {
      iconFile: IconCloudy,
      weatherTypes: 'Cloudy'
    },
    '04n': {
      iconFile: IconCloudy,
      weatherTypes: 'Cloudy'
    },
  }

export default weatherConditionIconIds;
</script>