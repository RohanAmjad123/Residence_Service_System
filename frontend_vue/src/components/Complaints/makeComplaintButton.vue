<template>
  <button type="button" @click="makeComplaint">Make Complaint</button>
</template>

<script>
export default {
  methods: {
    makeComplaint: function () {
      this.$router.push("/make-complaint");
    },
  },
};
</script>

<style></style>
