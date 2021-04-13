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
  </tr>
</template>

<script>
export default {
  props: ['maintreq'],
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
};
</script>

<style></style>

