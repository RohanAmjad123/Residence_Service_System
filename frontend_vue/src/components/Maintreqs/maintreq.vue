<template>
  <tr>
    <td>{{ requestID }}</td>
    <td>{{ studentID }}</td>
    <td>{{ technicianID }}</td>
    <td>{{ description }}</td>
    <td>{{ roomID }}</td>
    <td>{{ submissionDate }}</td>
    <td>{{ dateResolved }}</td>
    <td>{{ status }}</td>
    <td>{{ urgencyRating }}</td>
    <td v-if="status != 'RESOLVED' && ['technician'].includes(userRole)">
      <resolveMaintreqButton :maintreq="requestID" />
    </td>
    <td
      v-if="
        technicianID == null &&
        status != 'RESOLVED' &&
        ['admin'].includes(userRole)
      "
    >
      <assignMaintreqButton
        :maintreq="requestID"
        :technicians="this.technicians"
      />
    </td>
  </tr>
</template>

<script>
import resolveMaintreqButton from "@/components/Maintreqs/resolveMaintreqButton";
import assignMaintreqButton from "@/components/Maintreqs/assignMaintreqButton";

export default {
  components: {
    resolveMaintreqButton,
    assignMaintreqButton,
  },
  props: ["maintreq", "technicians"],
  data() {
    return {
      requestID: this.maintreq.request_id,
      studentID: this.maintreq.student_id,
      technicianID: this.maintreq.technician_id,
      description: this.maintreq.description,
      roomID: this.maintreq.room_id,
      submissionDate: this.maintreq.submit_date_time,
      dateResolved: this.maintreq.date_time_resolved,
      status: this.maintreq.status,
      urgencyRating: this.maintreq.urgency_rating,
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
