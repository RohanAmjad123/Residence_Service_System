<template>
  <div class="My Foodorders">
    <h1>My Food Orders</h1>
    <makeFoodorderButton
      class="btn btn-danger m-3 mb-4"
      v-if="['student'].includes(userRole)"
    />
    <foodordersTable class="container" />
  </div>
</template>

<script>
import foodordersTable from "@/components/Foodorders/foodordersTable";
import makeFoodorderButton from "@/components/Foodorders/makeFoodorderButton";

export default {
  components: {
    foodordersTable,
    makeFoodorderButton,
  },
  computed: {
    userRole: function () {
      return this.$store.state.role;
    },
  },
};
</script>

<style></style>
