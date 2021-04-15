<template>
  <table class="table">
    <thead class="table-secondary">
      <tr>
        <th>Order ID</th>
        <th>Student ID</th>
        <th>Chef ID</th>
        <th>Order Description</th>
        <th>Submission Date</th>
        <th>Date Fulfilled</th>
        <th>Status</th>
        <th v-if="['chef'].includes(userRole)"></th>
      </tr>
    </thead>
    <tbody>
      <foodorder
        v-for="foodorder in foodorders"
        :key="foodorder"
        :foodorder="foodorder"
      ></foodorder>
    </tbody>
  </table>
</template>

<script>
import foodorder from "@/components/Foodorders/foodorder";
import axios from "axios";

export default {
  components: {
    foodorder,
  },
  data() {
    return {
      foodorders: [],
      url: "",
    };
  },
  mounted() {
    let role = this.$store.state.role;
    let userID = this.$store.state.user.user_id;

    if (role == "student") {
      this.url = "students/" + userID + "/foodorders/";
    } else {
      this.url = "foodorders/";
    }

    axios
      .get(this.url)
      .then((response) => {
        this.foodorders = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  computed: {
    userRole: function () {
      return this.$store.state.role;
    },
  },
};
</script>

<style></style>
