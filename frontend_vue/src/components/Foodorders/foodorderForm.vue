<template>
  <div>
    <form>
      <div class="form-group">
        <label class="form-label">Student ID: {{ student_id }}</label>
      </div>
      <div class="form-group">
        <label class="form-label">Order Description</label>
        <input 
          type="text" 
          v-model="description"
          required
          class="form-control"
        />
      </div>
      <button type="submit" @click="submitFoodorder" class="btn btn-primary">Submit Food Order</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      description: "",
      student_id: this.$store.state.user.user_id,
    };
  },
  methods: {
    submitFoodorder: function () {
      let foodorder = {
        description: this.description,
        student_id: this.student_id,
      }
      axios.post("foodorders/", foodorder)
      .then(() => {
        this.$router.push("/myfoodorders")
      })
      .catch((error) => {
        console.log(error)
      })
    }
  }
};
</script>

<style></style>
