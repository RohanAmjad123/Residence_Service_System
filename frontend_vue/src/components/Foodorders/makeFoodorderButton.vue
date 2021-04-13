<template>
  <button type="button" @click="makeFoodorder">Make Food Order</button>
</template>

<script>
export default {
  methods: {
    makeFoodorder: function () {
      this.$router.push("/make-foodorder")
    }
  }
};
</script>

<style></style>
