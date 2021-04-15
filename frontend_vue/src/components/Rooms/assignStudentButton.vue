<template>
  <div class="dropdown">
    <button
      class="btn btn-success dropdown-toggle"
      type="button"
      id="dropdownMenuButton1"
      data-bs-toggle="dropdown"
      aria-expanded="false"
    >
      ASSIGN
    </button>
    <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
      <li
        class="dropdown-item"
        v-for="student in this.students"
        :key="student"
        @click="assign(student.user)"
      >
        Student ID: {{ student.user }} Name: {{ student.first_name }}
        {{ student.last_name }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["room", "students"],
  data() {
    return {
      roomID: this.room,
    };
  },
  methods: {
    assign: function (user) {
      let url = "rooms/" + this.roomID + "/";
      let data = {
        student_id: user,
      };
      axios
        .patch(url, data)
        .then(() => {
          this.$router.push("/managerooms");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
