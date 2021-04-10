<template>
<div>
<header><strong><center>Fullfill Food Orders</center></strong></header>
</div>
<div class="container">
  <div class="row">
    <div class="col-12">
      <table class="table table-bordered">
        <thead>
          <tr>
            <th scope="col">Student ID</th>
            <th scope="col">Food Order Description</th>
            <th scope="col">Name</th>
            <th scope="col">Fulfill?</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">1</th>
            <td>English Muffin and Bat Soup</td>
            <td>Firoz Lakhani</td>
            <td>
            <button type="button" class="btn btn-success"><i class="far fa-trash-alt"></i></button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</template>

<style>
.container {
  padding: 2rem 0rem;
}

h4 {
  margin: 2rem 0rem 1rem;
}

.table-image {
  td, th {
    vertical-align: middle;
  }
}
</style>


<script>
export default {
    
}
</script>