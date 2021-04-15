<template>
  <div class="btn-group">
    <button
      type="button"
      class="btn btn-success"
      @click="fulfill"
      v-if="status == 'IN PROGRESS'"
    >
      FULFILL
    </button>
    <button
      type="button"
      class="btn btn-warning"
      @click="start"
      v-if="status == 'UNFULFILLED'"
    >
      START
    </button>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";

export default {
  props: ["foodorder", "status"],
  data() {
    return {
      orderID: this.foodorder,
      orderStatus: this.status,
    };
  },
  methods: {
    start: function () {
      let url = "foodorders/" + this.orderID + "/";
      let data = {
        chef_id: this.$store.state.user.user_id,
        status: "IN PROGRESS",
      };
      axios
        .patch(url, data)
        .then(() => {
          this.$router.push("/myfoodorders");
        })
        .catch((error) => {
          console.log(error);
        });
    },
    fulfill: function () {
      let url = "foodorders/" + this.orderID + "/";
      let data = {
        chef_id: this.$store.state.user.user_id,
        date_time_resolved: moment().format("YYYY-MM-DD"),
        status: "FULFILLED",
      };
      axios
        .patch(url, data)
        .then(() => {
          this.$router.push("/myfoodorders");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
