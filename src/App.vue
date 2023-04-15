<template>
  <navhead />
  <router-view />
</template>

<script>
import Navhead from "@/components/NavHead.vue";
import variables from "@/main.js";

export default {
  name: "AppView",
  components: {
    Navhead,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: rgb(255, 118, 54);
}
</style>
