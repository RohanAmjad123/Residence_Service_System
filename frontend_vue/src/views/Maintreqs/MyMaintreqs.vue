<template>
  <div class="My Maintreqs">
    <h1 v-if="['student', 'technician'].includes(userRole)">
      My Maintenance Requests
    </h1>
    <h1 v-if="['admin'].includes(userRole)">Manage Maintenance Requests</h1>
    <makeMaintreqButton
      class="btn btn-danger m-3 mb-4"
      v-if="['student'].includes(userRole)"
    />
    <maintreqsTable class="container" />
  </div>
</template>

<script>
import maintreqsTable from "@/components/Maintreqs/maintreqsTable";
import makeMaintreqButton from "@/components/Maintreqs/makeMaintreqButton";

export default {
  components: {
    maintreqsTable,
    makeMaintreqButton,
  },
  computed: {
    userRole: function () {
      return this.$store.state.role;
    },
  },
};
</script>

<style></style>
