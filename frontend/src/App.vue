<template>
  <div id="app">
    <ImageHome></ImageHome>
  </div>
</template>

<script>
import ImageHome from './components/ImageHome.vue'

export default {
  name: 'App',
  components: {
    ImageHome
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
