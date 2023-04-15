<template>
  <div
    class="container-fluid justify-content-lg-center--"
    style="align-content: center"
  >
    <!--content d-flex justify-content-lg-center-->
    <div
      class="justify-content-lg-center row bg-white me-4"
      style="height: 100vh; width: 90vw"
    >
      <div class="col">
        <h1 class="Times p1">
          Get started your exciting
          <span class="text-orange">journey</span> with us.
        </h1>
        <p class="text-muted lucida p2">
          A Team of experienced tourism professionals will provide you with the
          best advice and tips for your desire place
        </p>
        <button class="btn button">Discover Now</button>
      </div>
      <div class="col bg-col">
        
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FV",
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
  .p1 {
    font-weight: bold;
    font-size: 80px;
  }
  .p2 {
    font-size: 23px;
  }

  .button {
    --bs-btn-color: rgb(255, 118, 54);
    --bs-btn-border-color: rgb(255, 118, 54);
    --bs-btn-hover-color: #fff;
    --bs-btn-hover-bg: rgb(255, 118, 54);
  }

  .bg-col{
            background-image: url('../../public/tourist-with-thumb-up__1_-removebg 1.png');
        }
}
</style>
