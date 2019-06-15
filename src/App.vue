<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Flash Card</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/vocabulary">Vocaulary</router-link> 
    </div>
    <router-view :vocabulary=vocabulary> </router-view>
  </div>
</template>

<script>
import json from '../gre_vocab.json'
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
export default {
  name: 'flashCard',
  components: {
    
  },
  data() {
    return {
      vocabulary: json
    }
  },
  methods: {
    removeCard: function(index){
      Vue.delete(this.vocabulary, index)
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
