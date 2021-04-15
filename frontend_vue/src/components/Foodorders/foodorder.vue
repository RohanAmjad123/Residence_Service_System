<template>
  <tr>
    <td>{{ orderID }}</td>
    <td>{{ studentID }}</td>
    <td>{{ chefID }}</td>
    <td>{{ description }}</td>
    <td>{{ submissionDate }}</td>
    <td>{{ dateFulfilled }}</td>
    <td>{{ status }}</td>
    <td v-if="status != 'FULFILLED' && ['chef'].includes(userRole)">
      <fulfillFoodorderButton :foodorder="orderID" :status="status" />
    </td>
  </tr>
</template>

<script>
import fulfillFoodorderButton from "@/components/Foodorders/fulfillFoodorderButton"

export default {
  components: {
    fulfillFoodorderButton
  },
  props: ["foodorder"],
  data() {
    return {
      orderID: this.foodorder.food_order_id,
      studentID: this.foodorder.student_id,
      chefID: this.foodorder.chef_id,
      description: this.foodorder.description,
      submissionDate: this.foodorder.submit_date_time,
      dateFulfilled: this.foodorder.date_time_fulfilled,
      status: this.foodorder.status,
    };
  },
  computed: {
    userRole: function () {
      return this.$store.state.role;
    },
  },
};
</script>

<style></style>
