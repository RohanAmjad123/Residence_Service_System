<template>
  <div class="My Complaints">
    <h1>My Complaints</h1>
    <makeComplaintButton class="btn btn-danger m-2"/>
    <complaintsTable class="container"/>
  </div>
</template>

<script>
import complaintsTable from "@/components/Complaints/complaintsTable";
import makeComplaintButton from "@/components/Complaints/makeComplaintButton";

export default {
  components: {
    complaintsTable,
    makeComplaintButton
  },
};
</script>

<style></style>
