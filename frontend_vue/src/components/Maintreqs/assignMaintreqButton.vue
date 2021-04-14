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
        v-for="technician in this.technicians"
        :key="technician"
        @click="assign(technician.user)"
      >
        Technician ID: {{ technician.user }} Name: {{ technician.first_name }}
        {{ technician.last_name }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["maintreq", "technicians"],
  data() {
    return {
      requestID: this.maintreq,
    };
  },
  methods: {
    assign: function (user) {
      let url = "maintreqs/" + this.requestID + "/";
      let data = {
        technician_id: user,
        status: "IN PROGRESS"
      };
      axios
        .patch(url, data)
        .then(() => {
          this.$router.push("/mymaintreqs");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
