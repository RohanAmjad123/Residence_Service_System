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
  </tr>
</template>

<script>
export default {
  props: ['complaint'],
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
};
</script>

<style></style>

