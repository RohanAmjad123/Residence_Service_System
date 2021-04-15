<template>
  <div class="container">
    <form class="container w-50" @submit.prevent="register">
      <h1>Register</h1>
      <div class="form-group">
        <label class="form-label m-2">Email</label>
        <input
          required
          v-model="email"
          type="email"
          placeholder="name@email.com"
          class="form-control"
        />
      </div>
      <div class="form-group">
        <label class="form-label m-2">Password</label>
        <input
          required
          v-model="password"
          type="password"
          placeholder="password"
          class="form-control"
        />
      </div>
      <div class="form-group">
        <label class="form-label m-2">First Name</label>
        <input
          required
          v-model="firstName"
          type="text"
          placeholder="First Name"
          class="form-control"
        />
      </div>
      <div class="form-group">
        <label class="form-label m-2">Last Name</label>
        <input
          required
          v-model="lastName"
          type="text"
          placeholder="Last Naem"
          class="form-control"
        />
      </div>
      <div class="form-group">
        <label class="form-label m-2">Phone Number</label>
        <input
          required
          v-model="phoneNum"
          type="tel"
          placeholder="Phone Number"
          class="form-control"
          pattern="[0-9]{10}"
        />
      </div>
      <div class="form-group">
        <div class="form-check m-2">
          <input
            class="form-check-input"
            type="radio"
            name="exampleRadios"
            id="exampleRadios1"
            value="student"
            checked
            v-model="type"
          />
          <label class="form-check-label" for="exampleRadios1"> Student </label>
        </div>
        <div class="form-check m-2">
          <input
            class="form-check-input"
            type="radio"
            name="exampleRadios"
            id="exampleRadios2"
            value="staff"
            v-model="type"
          />
          <label class="form-check-label" for="exampleRadios2">
            General Staff
          </label>
        </div>
        <div class="form-check m-2">
          <input
            class="form-check-input"
            type="radio"
            name="exampleRadios"
            id="exampleRadios3"
            value="admin"
            v-model="type"
          />
          <label class="form-check-label" for="exampleRadios3"> Admin </label>
        </div>
        <div class="form-check m-2">
          <input
            class="form-check-input"
            type="radio"
            name="exampleRadios"
            id="exampleRadios4"
            value="technician"
            v-model="type"
          />
          <label class="form-check-label" for="exampleRadios4">
            Technician
          </label>
        </div>
        <div class="form-check m-2">
          <input
            class="form-check-input"
            type="radio"
            name="exampleRadios"
            id="exampleRadios5"
            value="chef"
            v-model="type"
          />
          <label class="form-check-label" for="exampleRadios5"> Chef </label>
        </div>
      </div>
      <div class="form-group" v-if="type == 'student'">
        <label class="form-label m-2">Year Level</label>
        <div class="input-group">
          <select class="form-select" v-model="yearLevel" required>
            <option value="1" selected>1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
            <option value="5">5</option>
          </select>
        </div>
      </div>
      <div class="form-group" v-if="type == 'admin'">
        <label class="form-label m-2">Department</label>
        <input
          required
          v-model="department"
          type="text"
          placeholder="Department"
          class="form-control"
        />
      </div>
      <div class="form-group" v-if="type == 'technician'">
        <label class="form-label m-2">Specialization</label>
        <input
          required
          v-model="specialization"
          type="text"
          placeholder="Specialization"
          class="form-control"
        />
      </div>
      <div class="form-group" v-if="type == 'chef'">
        <label class="form-label m-2">Position</label>
        <input
          required
          v-model="position"
          type="text"
          placeholder="Position"
          class="form-control"
        />
      </div>
      <button type="submit" class="btn btn-primary m-3">Register</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  components: {},
  data() {
    return {
      email: "",
      password: "",
      firstName: "",
      lastName: "",
      phoneNum: "",
      type: "student",
      yearLevel: "",
      specialization: "",
      department: "",
      position: "",
    };
  },
  methods: {
    register: function () {
      let registerData = {};
      if (this.type == "student") {
        registerData = {
          user: {
            email: this.email,
            password: this.password,
            first_name: this.firstName,
            last_name: this.lastName,
            phone_num: this.phoneNum,
          },
          year_of_study: this.yearLevel,
        };
      } else if (this.type == "staff") {
        registerData = {
          user: {
            email: this.email,
            password: this.password,
            first_name: this.firstName,
            last_name: this.lastName,
            phone_num: this.phoneNum,
          },
        };
      } else if (this.type == "admin") {
        registerData = {
          user: {
            email: this.email,
            password: this.password,
            first_name: this.firstName,
            last_name: this.lastName,
            phone_num: this.phoneNum,
          },
          department: this.department,
        };
      } else if (this.type == "technician") {
        registerData = {
          user: {
            email: this.email,
            password: this.password,
            first_name: this.firstName,
            last_name: this.lastName,
            phone_num: this.phoneNum,
          },
          specialization: this.specialization,
        };
      } else if (this.type == "chef") {
        registerData = {
          user: {
            email: this.email,
            password: this.password,
            first_name: this.firstName,
            last_name: this.lastName,
            phone_num: this.phoneNum,
          },
          position: this.position,
        };
      }
      let url = "register/" + this.type + "/";

      let loginData = {
        email: this.email,
        password: this.password,
      };

      axios
        .post(url, registerData)
        .then(() => {
          this.$store.dispatch("login", loginData).then(() => {
            this.$router.push("/dashboard");
          });
        })
        .catch((error) => {
          console.log("it did not work");
          console.log(error);
        });
    },
  },
};
</script>

<style></style>
