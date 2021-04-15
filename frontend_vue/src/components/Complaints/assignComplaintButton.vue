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
        v-for="staff in this.staff"
        :key="staff"
        @click="assign(staff.user)"
      >
        Staff ID: {{ staff.user }} Name: {{ staff.first_name }}
        {{ staff.last_name }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["complaint", "staff"],
  data() {
    return {
      complaintID: this.complaint,
    };
  },
  methods: {
    assign: function (user) {
      let url = "complaints/" + this.complaintID + "/";
      let data = {
        staff_id: user,
        status: "IN PROGRESS",
      };
      axios
        .patch(url, data)
        .then(() => {
          this.$router.push("/mycomplaints");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
