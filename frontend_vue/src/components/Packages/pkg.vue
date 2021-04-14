<template>
  <tr>
    <td>{{ packageID }}</td>
    <td>{{ studentID }}</td>
    <td>{{ dateRecieved }}</td>
  </tr>
</template>

<script>
export default {
  props: ['pkg'],
  data() {
    return {
      packageID: this.pkg.package_id,
      studentID: this.pkg.student_id,
      dateRecieved: this.pkg.date_recieved,
    };
  },
};
</script>

<style></style>

