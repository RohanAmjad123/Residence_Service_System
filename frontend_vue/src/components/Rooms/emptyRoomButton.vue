<template>
  <div class="dropdown">
    <button class="btn btn-danger" type="button" @click="empty">EMPTY</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["room"],
  data() {
    return {
      roomID: this.room,
    };
  },
  methods: {
    empty: function () {
      let url = "rooms/" + this.roomID + "/";
      let data = {
        student_id: null,
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
