<template>
  <div class="dropdown">
    <button
      class="btn btn-danger dropdown-toggle"
      type="button"
      id="dropdownMenuButton1"
      data-bs-toggle="dropdown"
      aria-expanded="false"
    >
      ADD PACKAGE
    </button>
    <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
      <li
        class="dropdown-item"
        v-for="student in students"
        :key="student"
        @click="addPackage(student.user)"
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
  data() {
    return {
      students: [],
    };
  },
  mounted() {
    axios
      .get("students/")
      .then((response) => {
        this.students = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    addPackage: function (user) {
      let data = {
        student_id: user,
      };
      axios
        .post("packages/", data)
        .then(() => {
          this.$router.push("/mypackages");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style></style>
