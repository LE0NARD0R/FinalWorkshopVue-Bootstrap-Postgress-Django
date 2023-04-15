<template>
  <div class="bg-light">
    <div class="container-fluid" style="width: 40vw">
      <h1 class="justify-content-lg-center Times p3" style="text-align: center">
        Things you need <span class="text-orange">to do</span>
      </h1>
      <p class="lucida text-muted" style="text-align: center; font-size: 18px">
        We ensure that you'll embark on a perfectly planned, safe vacation at a
        price you can afford.
      </p>
    </div>
    <div class="card-deck" style="height: 40vh; width: 90vw">
      <div class="row centrado">
        <div class="col">
          <div
            class="card shadow p-3 mb-5 bg-white rounded"
            style="height: 40vh; width: 28vw"
          >
            <img
              class="card-img-top pic"
              v-bind:src="require('../../public/Group1.png')"
            />

            <div class="card-body izquierda">
              <h5 class="card-title negrilla">Sign Up</h5>
              <p class="card-text text-muted">
                Completes all the work associated with planning and procesing
              </p>
            </div>
          </div>
        </div>
        <div class="col">
          <div
            class="card shadow p-3 mb-5 bg-white rounded"
            style="height: 40vh; width: 28vw"
          >
            <img
              class="card-img-top pic"
              v-bind:src="require('../../public/Group2.png')"
            />
            <div class="card-body izquierda">
              <h5 class="card-title negrilla">Worth of Money</h5>
              <p class="card-text text-muted">
                After successfull access then book from exclusive deals &
                pricing
              </p>
            </div>
          </div>
        </div>
        <div class="col">
          <div
            class="card shadow p-3 mb-5 bg-white rounded"
            style="height: 40vh; width: 28vw"
          >
            <img
              class="card-img-top pic"
              v-bind:src="require('../../public/Group3.png')"
            />
            <div class="card-body izquierda">
              <h5 class="card-title negrilla">Exciting Trabel</h5>
              <p class="card-text text-muted">
                Start and explore a wide range of exciting travel expierience
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FirstCard",
};
</script>

<style lang="scss" scoped>
::v-deep {
  .text-orange {
    color: rgb(255, 118, 54);
  }
  .Times {
    font-family: Times New Roman, Times, serif;
  }
  .lucida {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
  }
  .p3 {
    font-weight: bold;
    font-size: 50px;
  }

  .pic {
    height: 10vh;
    width: 5vw;
    padding-left: 10px;
    padding-top: 10px;
  }
  .izquierda {
    text-align: left;
  }
  .negrilla {
    font-weight: bold;
  }
  .centrado{
    justify-content: center;
  }
}
</style>
