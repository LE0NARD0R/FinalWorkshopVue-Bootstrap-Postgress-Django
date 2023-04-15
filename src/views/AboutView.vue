<template>
  <fv />
  <qoute />
  <fc />
  <br />
  <br />
  <br />
  <sc />
</template>

<script>
import fv from "@/components/FirstView.vue";
import qoute from "@/components/quote.vue";
import fc from "@/components/FirstCard.vue";
import sc from '@/components/SecondCard.vue'

export default {
  name: "AboutView",
  components: {
    fv,
    qoute,
    fc,
    sc,
  },
};
</script>
