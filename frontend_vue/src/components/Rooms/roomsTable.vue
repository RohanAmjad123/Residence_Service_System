<template>
  <table class="table">
    <thead class="table-secondary">
      <tr>
        <th>Building ID</th>
        <th>Building Name</th>
        <th>Year Level</th>
        <th>Building Location</th>
        <th>Room ID</th>
        <th>Room Number</th>
        <th>Student ID</th>
        <th v-if="['staff', 'admin'].includes(userRole)"></th>
      </tr>
    </thead>
    <tbody>
      <room
        v-for="room in rooms"
        :key="room"
        :room="room"
        :students="students"
      ></room>
    </tbody>
  </table>
</template>

<script>
import room from "@/components/Rooms/room";
import axios from "axios";

export default {
  components: {
    room,
  },
  data() {
    return {
      rooms: [],
      students: [],
    };
  },
  mounted() {
    axios
      .get("rooms/?sort_by=building_id")
      .then((response) => {
        this.rooms = response.data;
      })
      .catch((error) => {
        console.log(error);
      });

    axios
      .get("students/?without_room=true")
      .then((response) => {
        this.students = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
    console.log(this.rooms);
    console.log(this.students);
  },
  computed: {
    userRole: function () {
      return this.$store.state.role;
    },
  },
};
</script>

<style></style>
