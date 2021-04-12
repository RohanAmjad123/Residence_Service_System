<template>
  <div class="navbar navbar-light bg-light">
    <div class="container-fluid">
        <router-link to="Home" v-if="!isLoggedIn" class="navbar-brand">Home</router-link>
        <router-link to="Login" v-if="!isLoggedIn" class="navbar-brand">Login</router-link>
        <router-link to="Dashboard" v-if="isLoggedIn" class="navbar-brand">Dashboard</router-link>
        <router-link to="MyComplaints" v-if="isLoggedIn" class="navbar-brand">My Complaints</router-link>
        <logoutButton v-if="isLoggedIn" />
      </div>
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
