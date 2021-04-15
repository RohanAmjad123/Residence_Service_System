<template>
  <div class="navbar navbar-dark bg-dark mb-5">
    <div class="d-flex flex-row px-4">
      <router-link to="Home" v-if="!isLoggedIn" class="navbar-brand"
        >Home
      </router-link>
      <router-link to="Dashboard" v-if="isLoggedIn" class="navbar-brand"
        >Dashboard
      </router-link>
      <router-link
        to="MyComplaints"
        v-if="isLoggedIn && ['student', 'staff'].includes(userRole)"
        class="navbar-brand"
        >My Complaints
      </router-link>
      <router-link
        to="MyComplaints"
        v-if="isLoggedIn && ['admin'].includes(userRole)"
        class="navbar-brand"
        >Manage Complaints
      </router-link>
      <router-link
        to="MyMaintreqs"
        v-if="isLoggedIn && ['student', 'technician'].includes(userRole)"
        class="navbar-brand"
        >My Maintenance Requests
      </router-link>
      <router-link
        to="MyMaintreqs"
        v-if="isLoggedIn && ['admin'].includes(userRole)"
        class="navbar-brand"
        >Manage Maintenance Requests
      </router-link>
      <router-link
        to="MyFoodorders"
        v-if="isLoggedIn && ['student'].includes(userRole)"
        class="navbar-brand"
        >My Food Orders
      </router-link>
      <router-link
        to="MyFoodorders"
        v-if="isLoggedIn && ['chef'].includes(userRole)"
        class="navbar-brand"
        >Manage Food Orders
      </router-link>
      <router-link
        to="MyFoodorders"
        v-if="isLoggedIn && ['admin'].includes(userRole)"
        class="navbar-brand"
        >Food Orders
      </router-link>
      <router-link
        to="MyPackages"
        v-if="isLoggedIn && ['student'].includes(userRole)"
        class="navbar-brand"
        >My Packages
      </router-link>
      <router-link
        to="MyPackages"
        v-if="isLoggedIn && ['staff', 'admin'].includes(userRole)"
        class="navbar-brand"
        >Manage Packages
      </router-link>
      <router-link
        to="ManageRooms"
        v-if="isLoggedIn && ['staff', 'admin'].includes(userRole)"
        class="navbar-brand"
        >Manage Rooms
      </router-link>
    </div>
    <div class="d-flex flex-row px-4">
      <logoutButton
        v-if="isLoggedIn"
        class="btn btn-secondary navbar-brand ml-3 px-3"
      />
      <router-link
        to="Register"
        v-if="!isLoggedIn"
        class="btn btn-secondary navbar-brand ml-3 px-3"
        >Register</router-link
      >
      <router-link
        to="Login"
        v-if="!isLoggedIn"
        class="btn btn-primary navbar-brand ml-3 px-3"
        >Login</router-link
      >
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
    userRole: function () {
      return this.$store.state.role;
    },
  },
};
</script>

<style></style>
