<template>
  <div class="btn-group">
    <button type="button" class="btn btn-success" @click="resolve">
      RESOLVE
    </button>
    <button
      type="button"
      class="btn btn-success dropdown-toggle dropdown-toggle-split"
      data-bs-toggle="dropdown"
      aria-expanded="false"
    >
      <span class="visually-hidden">Toggle Dropdown</span>
    </button>
    <ul class="dropdown-menu">
      <li>
        <input
          class="dropdown-item"
          v-model="resolution_description"
          placeholder="resolution description"
        />
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";

export default {
  props: ["complaint"],
  data() {
    return {
      complaintID: this.complaint,
      resolution_description: "",
    };
  },
  methods: {
    resolve: function () {
      let url = "complaints/" + this.complaintID + "/";
      let data = {
        resolution_description: this.resolution_description,
        date_time_resolved: moment().format("YYYY-MM-DD"),
        status: "RESOLVED",
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
