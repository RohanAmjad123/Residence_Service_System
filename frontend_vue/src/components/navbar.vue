<template>
  <div class="navbar navbar-dark bg-dark mb-5">
      <div class="d-flex flex-row px-4">
        <router-link to="Home" v-if="!isLoggedIn" class="navbar-brand">Home</router-link>
        <router-link to="Dashboard" v-if="isLoggedIn" class="navbar-brand">Dashboard</router-link>
        <router-link to="MyComplaints" v-if="isLoggedIn" class="navbar-brand">My Complaints</router-link>
      </div>
      <logoutButton v-if="isLoggedIn" class="btn btn-secondary navbar-brand ml-3 px-3" />
      <router-link to="Login" v-if="!isLoggedIn" class="btn btn-primary navbar-brand ml-3 px-3">Login</router-link>
  </div>
</template>

<script>
import logoutButton from "@/components/logoutButton";

export default {
  name: "navbar",
  components: {
    logoutButton,
  },
  computed: {
    isLoggedIn: function () {
      return this.$store.getters.isLoggedIn;
    },
  },
};
</script>

<style></style>
