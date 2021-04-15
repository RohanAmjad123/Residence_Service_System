<template>
  <div class="Manage Rooms">
    <h1>Manage Rooms</h1>
    <roomsTable class="container" />
  </div>
</template>

<script>
import roomsTable from "@/components/Rooms/roomsTable";

export default {
  components: {
    roomsTable,
  },
  computed: {
    userRole: function () {
      return this.$store.state.role;
    },
  },
};
</script>

<style></style>
