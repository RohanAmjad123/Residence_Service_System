<template>
  <tr>
    <td>{{ buildingID }}</td>
    <td>{{ buildingName }}</td>
    <td>{{ yearLevel }}</td>
    <td>{{ buildingLocation }}</td>
    <td>{{ roomID }}</td>
    <td>{{ roomNo }}</td>
    <td>{{ studentID }}</td>
    <td v-if="studentID != null && ['staff', 'admin'].includes(userRole)">
      <emptyRoomButton :room="roomID" />
    </td>
    <td v-if="studentID == null && ['staff', 'admin'].includes(userRole)">
      <assignStudentButton :room="roomID" :students="this.students" />
    </td>
  </tr>
</template>

<script>
import emptyRoomButton from "@/components/Rooms/emptyRoomButton";
import assignStudentButton from "@/components/Rooms/assignStudentButton";

export default {
  components: {
    emptyRoomButton,
    assignStudentButton,
  },
  props: ["room", "students"],
  data() {
    return {
      buildingID: this.room.building_id,
      buildingName: this.room.building_name,
      yearLevel: this.room.year_level,
      buildingLocation: this.room.building_location,
      roomID: this.room.room_id,
      roomNo: this.room.room_no,
      studentID: this.room.student_id,
    };
  },
  computed: {
    userRole: function () {
      return this.$store.state.role;
    },
  },
};
</script>

<style></style>
