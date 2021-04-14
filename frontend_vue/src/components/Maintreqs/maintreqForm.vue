<template>
  <div class="container w-50">
    <form>
      <div class="form-group">
        <label class="form-label">Student ID: {{ student_id }}</label>
      </div>
      <div class="form-group">
        <label class="form-label">Problem Description</label>
        <input 
          type="text" 
          v-model="description"
          required
          class="form-control"
        />
      </div>
      <div class="form-group">
        <label class="form-label">Urgency Rating</label>
        <div class="input-group">
          <select class="form-select" v-model="urgency_rating">
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
          </select>
        </div>
      </div>
      <button type="submit" @click="submitMaintreq" class="btn btn-primary">Submit Maintenance Request</button>
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
      urgency_rating: ""
    };
  },
  methods: {
    submitMaintreq: function () {
      let maintreq = {
        description: this.description,
        student_id: this.student_id,
        urgency_rating: this.urgency_rating
      }
      axios.post("maintreqs/", maintreq)
      .then(() => {
        this.$router.push("/mymaintreqs")
      })
      .catch((error) => {
        console.log(error)
      })
    }
  }
};
</script>

<style></style>
