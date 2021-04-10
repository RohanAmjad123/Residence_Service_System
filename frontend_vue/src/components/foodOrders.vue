<template>
   <div class="container">
  <div class="row">
    <div class="col-12">
      <table class="table table-bordered">
        <thead>
          <tr>
            <th scope="col">Food Order ID</th>
            <th scope="col">Food Order Description</th>
            <th scope="col">Status</th>
            <th scope="col">Remove?</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">1</th>
            <td>English Muffin and Bat Soup</td>
            <td>Ready</td>
            <td>
            <button type="button" class="btn btn-danger"><i class="far fa-trash-alt"></i></button>
            </td>
          </tr>
          <tr>
            <th scope="row">2</th>
            <td>Potatoes x 4 and a fried egg</td>
            <td>Not Ready</td>
            <td>
            <button type="button" class="btn btn-danger"><i class="far fa-trash-alt"></i></button>
            </td>
          </tr>
          <tr>
            <th scope="row">3</th>
            <td>goth girl saliva</td>
            <td>Ready</td>
            <td>
            <button type="button" class="btn btn-danger"><i class="far fa-trash-alt"></i></button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</template>

<script>
export default {
    
}
</script>