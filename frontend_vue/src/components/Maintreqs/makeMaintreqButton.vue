<template>
  <button type="button" @click="makeMaintreq">Make Maintenance Request</button>
</template>

<script>
export default {
  methods: {
    makeMaintreq: function () {
      this.$router.push("/mymaintreqs");
    },
  },
};
</script>

<style></style>
