<template>
  <div>
    <form>
      <div class="form-group">
        <label class="form-label">Student ID: {{ student_id }}</label>
      </div>
      <div class="form-group">
        <label class="form-label">Problem Description</label>
        <input 
          type="text" 
          v-model="problem_description"
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
      <button type="submit" @click="submitComplaint" class="btn btn-primary">Submit Complaint</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      problem_description: "",
      student_id: this.$store.state.user.user_id,
      urgency_rating: ""
    };
  },
  methods: {
    submitComplaint: function () {
      let complaint = {
        problem_description: this.problem_description,
        student_id: this.student_id,
        urgency_rating: this.urgency_rating
      }
      axios.post("complaints/", complaint)
      .then(() => {
        this.$router.push("/my-complaints")
      })
      .catch((error) => {
        console.log(error)
      })
    }
  }
};
</script>

<style></style>
