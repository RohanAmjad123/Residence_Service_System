<template>
  <button type="button" @click="logout">Log Out</button>
</template>

<script>
export default {
  methods: {
    logout: function () {
      this.$store.dispatch("logout").then(() => {
        this.$router.push("/home");
      });
    },
  },
};
</script>
