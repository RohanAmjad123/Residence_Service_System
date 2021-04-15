<template>
  <div class="My Complaints">
    <h1 v-if="['student', 'staff'].includes(userRole)">My Complaints</h1>
    <h1 v-if="['admin'].includes(userRole)">Manage Complaints</h1>
    <makeComplaintButton
      class="btn btn-danger m-3 mb-4"
      v-if="['student'].includes(userRole)"
    />
    <complaintsTable class="container" />
  </div>
</template>

<script>
import complaintsTable from "@/components/Complaints/complaintsTable";
import makeComplaintButton from "@/components/Complaints/makeComplaintButton";

export default {
  components: {
    complaintsTable,
    makeComplaintButton,
  },
  computed: {
    userRole: function () {
      return this.$store.state.role;
    },
  },
};
</script>

<style></style>
