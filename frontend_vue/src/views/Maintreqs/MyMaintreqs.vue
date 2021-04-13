<template>
  <div class="My Maintreqs">
    <h1>My Maintenance Requests</h1>
    <makeMaintreqButton class="btn btn-danger m-2"/>
    <maintreqsTable class="container"/>
  </div>
</template>

<script>
import maintreqsTable from "@/components/Maintreqs/maintreqsTable";
import makeMaintreqButton from "@/components/Maintreqs/makeMaintreqButton";

export default {
  components: {
    maintreqsTable,
    makeMaintreqButton
  },
};
</script>

<style></style>
