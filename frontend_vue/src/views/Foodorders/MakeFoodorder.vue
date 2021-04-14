<template>
  <div class="MakeFoodorder">
    <h1>Submit Food Order</h1>
    <foodorderForm />
  </div>
</template>

<script>
import foodorderForm from "@/components/Foodorders/foodorderForm";

export default {
  components: {
    foodorderForm,
  },
};
</script>
