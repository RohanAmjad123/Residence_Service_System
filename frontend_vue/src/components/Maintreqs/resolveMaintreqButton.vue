<template>
  <div class="btn-group">
    <button type="button" class="btn btn-success" @click="resolve">
      RESOLVE
    </button>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";

export default {
  props: ["maintreq"],
  data() {
    return {
      maintreqID: this.maintreq,
    };
  },
  methods: {
    resolve: function () {
      let url = "maintreqs/" + this.maintreqID + "/";
      let data = {
        date_time_resolved: moment().format("YYYY-MM-DD"),
        status: "RESOLVED",
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
