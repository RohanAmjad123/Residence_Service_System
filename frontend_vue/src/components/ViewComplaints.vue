<template>
<div>
<h1> View My Complaints </h1>
<table class="styled-table">
    <thead>
        <tr>
            <th>Name</th>
            <th>StudentID</th>
            <th>Urgency Rating</th>
            <th>Status</th>
            
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>{{name}}</td>
            <td>{{studentID}}</td>
            <td>{{Urgency}}</td>
            <th><button>Update</button></th>
        </tr>
        
        <!-- and so on... -->
    </tbody>
    <tbody>
        <tr>
            <td>Sajid Hafiz</td>
            <td>{{600791234}}</td>
            <td>{{5}}</td>
            <th><button>Update</button></th>
        </tr>
        
        <!-- and so on... -->
    </tbody>
</table>
</div>
  
</template>

<script>


export default {
   data:() => {
       return{
           name: 'Firoz Lakhani',
           studentID: '30071271',
           Urgency: 3,   
       }
   }
}
</script>

<style scoped>
.styled-table {
    border-collapse: collapse;
    margin-left: auto;
    margin-right: auto;
    font-size: 0.9em;
    font-family: sans-serif;
    min-width: 400px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
}
.styled-table thead tr {
    background-color: #009879;
    color: #ffffff;
    text-align: left;
}
.styled-table th,
.styled-table td {
    padding: 12px 15px;
}
.styled-table tbody tr {
    border-bottom: 1px solid #dddddd;
}

.styled-table tbody tr:nth-of-type(even) {
    background-color: #f3f3f3;
}

.styled-table tbody tr:last-of-type {
    border-bottom: 2px solid #009879;
}
.styled-table tbody tr.active-row {
    font-weight: bold;
    color: #009879;
}

</style>
