<template>
  <nav
    class="navbar navbar-expand-lg bg-with rounded"
    aria-label="Thirteenth navbar example"
  >
    <div class="container-fluid">
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarsExample11"
        aria-controls="navbarsExample11"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse d-lg-flex" id="navbarsExample11">
        <a class="navbar-brand col-lg-3 me-0" href="#">
          <img v-bind:src="require('../../public/Logo.png')" />
        </a>
        <ul class="navbar-nav col-lg-6 justify-content-lg-center">
          <li class="nav-item">
            <router-link to="/"
              ><span class="material-icons-outlined">home </span
              > <br>Home</router-link
            >
          </li>
          <li class="nav-item push">
            <router-link to="/about"
              ><span class="material-icons-outlined">
                help_outline
              </span><br>About</router-link
            >
          </li>
          <li class="nav-item push">
            <router-link to="/destination"
              ><span class="material-icons-outlined">
                flight_takeoff
              </span><br>Destination</router-link
            >
          </li>
          <li class="nav-item push">
            <router-link to="/tour"
              ><span class="material-icons-outlined"> map </span>
            <br> Tour</router-link
            >
          </li>
          <li class="nav-item push">
            <router-link to="/blog"
              ><span class="material-icons-outlined"> newspaper </span>
            <br> Blog</router-link
            >
          </li>
        </ul>
        <div class="d-lg-flex col-lg-3 justify-content-lg-end">
          <button class="btn btn-white text-orange" style="width: 120px">
            Login
          </button>
          <button
            class="btn bg-orange text-white"
            style="box-shadow: 0, 0, 35px rgba(252, 84, 0, 0.86); width: 120px"
          >
            Sing up</button
          ><!-- corregir el botón-->
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navhead",
};
</script>

<style lang="scss" scoped>
::v-deep {
  .text-orange {
    color: rgb(255, 118, 54);
  }
  .bg-orange {
    background-color: rgb(255, 98, 25);
  }

  .push {
    margin-left: 20px;
  }
}
</style>
