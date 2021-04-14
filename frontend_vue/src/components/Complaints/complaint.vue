<template>
  <tr>
    <td>{{ complaintID }}</td>
    <td>{{ studentID }}</td>
    <td>{{ staffID }}</td>
    <td>{{ description }}</td>
    <td>{{ resolutionDescription }}</td>
    <td>{{ submissionDate }}</td>
    <td>{{ dateResolved }}</td>
    <td>{{ status }}</td>
    <td>{{ urgencyRating }}</td>
    <td v-if="status != 'RESOLVED' && ['staff'].includes(userRole)">
      <resolveComplaintButton :complaint="complaintID" />
    </td>
    <td
      v-if="
        staffID == null && status != 'RESOLVED' && ['admin'].includes(userRole)
      "
    >
      <assignComplaintButton :complaint="complaintID" :staff="this.staff" />
    </td>
  </tr>
</template>

<script>
import resolveComplaintButton from "@/components/Complaints/resolveComplaintButton";
import assignComplaintButton from "@/components/Complaints/assignComplaintButton";

export default {
  components: {
    resolveComplaintButton,
    assignComplaintButton,
  },
  props: ["complaint", "staff"],
  data() {
    return {
      complaintID: this.complaint.complaint_id,
      studentID: this.complaint.student_id,
      staffID: this.complaint.staff_id,
      description: this.complaint.problem_description,
      resolutionDescription: this.complaint.resolution_description,
      submissionDate: this.complaint.submit_date_time,
      dateResolved: this.complaint.date_time_resolved,
      status: this.complaint.status,
      urgencyRating: this.complaint.urgency_rating,
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
