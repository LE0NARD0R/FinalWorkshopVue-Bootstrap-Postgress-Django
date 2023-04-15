<template>
  <div class="container-fluid" style="width: 60vw">
    <div class="card shadow p-3 mb-5 bg-white rounded-5">
      <div class="card-body">
        <div class="row">
          <div class="col" style="width: 25vw">
            <button class="btn btn-white dropdown-toggle">Location</button>
            <p class="text-muted" style="padding: 12px; font-size: small">
              Where are you going
            </p>
          </div>
          <div class="col" style="width: 25vw">
            <button class="btn btn-white dropdown-toggle">Date</button>
            <p class="text-muted" style="padding: 12px; font-size: small">
              When you will go
            </p>
          </div>
          <div class="col" style="width: 25vw">
            <button class="btn btn-white dropdown-toggle">Guest</button>
            <p class="text-muted" style="padding: 12px; font-size: small">
              Number of guest
            </p>
          </div>
          <div class="col" style="width: 25vw">
            <button
              class="btn bg-orange text-white btn-lg"
              style="height: 11vh"
            >
              Explore Now
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PruebaQuote",
};
</script>

<style lang="scss" scoped>
::v-deep {
  .bg-orange {
    background-color: rgb(255, 98, 25);
  }
}
</style>
