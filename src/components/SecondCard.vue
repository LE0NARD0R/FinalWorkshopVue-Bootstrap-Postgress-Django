<template>
  <div class="bg-white">
    <div class="container-fluid" style="width: 45vw">
      <h1 class="justify-content-lg-center Times p3" style="text-align: center">
        Exclusive <span class="text-orange">deals & discounts</span>
      </h1>
    </div>
    <div class="container-fluid" style="width: 40vw">
      <p class="lucida text-muted" style="text-align: center; font-size: 18px">
        Discover our fantastic early booking discounts & start planning your
        journey.
      </p>
    </div>
    <div class="card-deck cartas">
      <div class="row centrado">
        <div
          v-for="place in places"
          class="card shadow p-3 mb-5 bg-white rounded cartitas"
        >
          <img
            class="card-img-top pic"
            v-bind:src="PhotoPath+PhotoRoute"
          />
          <div class="card-body izquierda row">
            <div class="col">
              <h5 class="card-title negrilla">{{ place.PlaceName }}</h5>
              <p class="card-text text-muted p2">
                <span class="material-icons-outlined"> place </span>
                {{ place.PlaceLocation }}
              </p>
            </div>
            <div class="col derecha">
              <p class="card-text text-muted p2">
                <span class="material-icons-two-tone"> star </span>
                {{ place.PlaceRate }}
              </p>
              <button class="btn button text-orange">
                {{ place.PlacePrice }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import variables from "@/main.js";
import axios from "axios";

export default {
  name: "SecondCard",

  data() {
    return {
      places: [],
      PhotoRoute: [],
    };
  },

  methods: {
    refreshData() {
      axios.get(variables.API_URL + "places").then((response) => {
        alert("it works");
        this.places = response.data;
        this.PhotoRoute = places.PhotoPlace;
      });
    },
  },
  mounted: function () {
    this.refreshData();
  },
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
  .Times {
    font-family: Times New Roman, Times, serif;
  }
  .lucida {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
  }
  .p1 {
    font-weight: bold;
    font-size: 80px;
  }
  .p2 {
    font-size: 13px;
  }
  .button {
    background-color: rgba(238, 199, 156, 0.932);
  }
  .p3 {
    font-weight: bold;
    font-size: 50px;
  }
  .izquierda {
    text-align: left;
  }
  .derecha {
    text-align: right;
  }
  .negrilla {
    font-weight: bold;
  }
  .centrado {
    justify-content: center;
  }

  .cartas {
    height: 60vh;
    width: 90vw;
  }

  .cartitas {
    height: 60vh;
    width: 18vw;
  }

  .pic {
    height: 40vh;
    width: 15.6vw;
    text-align: center;
  }
}
</style>
