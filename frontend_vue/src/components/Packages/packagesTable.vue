<template>
  <table class="table">
    <thead class="table-secondary">
      <tr>
        <th>Package ID</th>
        <th>Student ID</th>
        <th>Date Recieved</th>
      </tr>
    </thead>
    <tbody>
      <pkg v-for="pkg in packages" :key="pkg" :pkg="pkg"> </pkg> 
    </tbody>
  </table>
</template>

<script>
import pkg from "@/components/Packages/pkg";
import axios from "axios";

export default {
  components: {
    pkg,
  },
  data() {
    return {
      packages: [],
      url: ""
    }
  },
  mounted() {
    let role = this.$store.state.role
    let userID = this.$store.state.user.user_id;

    if (role == "student") {
        this.url = "students/" + userID + "/packages/";
    }
    else {
      this.url = "packages/"
    }

    axios.get(this.url)
    .then(response => {
      this.packages = response.data;
    })
    .catch((error) => {
      console.log(error)
    })
  }
};
</script>

<style>
</style>
