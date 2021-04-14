<template>
  <div class="My Packages">
    <h1>My Packages</h1>
    <addPackageButton
      class="btn btn-danger m-3 mb-4"
      v-if="['staff', 'admin'].includes(userRole)"
    />
    <packagesTable class="container" />
  </div>
</template>

<script>
import packagesTable from "@/components/Packages/packagesTable";
import addPackageButton from "@/components/Packages/addPackageButton";

export default {
  components: {
    packagesTable,
    addPackageButton,
  },
  computed: {
    userRole: function () {
      return this.$store.state.role;
    },
  },
};
</script>

<style></style>
