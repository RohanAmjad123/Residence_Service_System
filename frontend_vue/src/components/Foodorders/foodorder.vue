<template>
  <tr>
    <td>{{ orderID }}</td>
    <td>{{ studentID }}</td>
    <td>{{ chefID }}</td>
    <td>{{ description }}</td>
    <td>{{ submissionDate }}</td>
    <td>{{ dateFulfilled }}</td>
    <td>{{ status }}</td>
  </tr>
</template>

<script>
export default {
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
};
</script>

<style></style>
