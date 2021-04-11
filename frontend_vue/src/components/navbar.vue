<template>
  <div class="nav">
    <router-link to="Home" v-if="!isLoggedIn">Home</router-link>
    <router-link to="Login" v-if="!isLoggedIn">Login</router-link>
    <router-link to="Dashboard" v-if="isLoggedIn">Dashboard</router-link>
    <router-link to="MyComplaints" v-if="isLoggedIn">My Complaints</router-link>
    <logoutButton v-if="isLoggedIn" />
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
