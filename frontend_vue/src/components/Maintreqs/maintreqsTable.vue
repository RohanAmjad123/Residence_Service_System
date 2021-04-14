<template>
  <table class="table">
    <thead class="table-secondary">
      <tr>
        <th>Request ID</th>
        <th>Student ID</th>
        <th>Technician ID</th>
        <th>Description</th>
        <th>Room ID</th>
        <th>Submission Date</th>
        <th>Date Resolved</th>
        <th>Status</th>
        <th>Urgency Rating</th>
      </tr>
    </thead>
    <tbody>
      <maintreq v-for="maintreq in maintreqs" :key="maintreq" :maintreq="maintreq"> </maintreq> 
    </tbody>
  </table>
</template>

<script>
import maintreq from "@/components/Maintreqs/maintreq";
import axios from "axios";

export default {
  components: {
    maintreq,
  },
  data() {
    return {
      maintreqs: [],
      url: ""
    }
  },
  mounted() {
    let role = this.$store.state.role
    let userID = this.$store.state.user.user_id;

    if (role == "student") {
        this.url = "students/" + userID + "/maintreqs/";
    }
    else if (role == "technician") {
        this.url = "technicians/" + userID + "/maintreqs/"
    }
    else {
      this.url = "maintreqs/"
    }

    axios.get(this.url)
    .then(response => {
      this.maintreqs = response.data;
    })
    .catch((error) => {
      console.log(error)
    })
  }
};
</script>

<style>
</style>
