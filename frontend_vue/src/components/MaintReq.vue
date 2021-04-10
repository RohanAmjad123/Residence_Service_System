<template>
<div>
    <h1>Maintenance Request Form</h1>
    <p>Student Name: {{name}}</p>
    <p>ID: {{studentID}}</p>
    <p>Building: {{Building}}</p>
    <p>Room: {{Room_no}}</p>
    <form action="/action_page.php">
        <textarea name="message" rows="10" cols="30">The cat was playing in the garden.</textarea>
    <br><br>
     <input type="submit">
    </form>
    
</div>
    
</template>

<script>

export default {
   data:() => {
       return{
           name: 'Firoz Lakhani',
           studentID: '30071271',
           Building: 'Yemnuska',
           Room_no: 348
       }
   }
}
</script>

<style scoped>

</style>
