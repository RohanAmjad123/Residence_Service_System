<template>
  <div class="container">
    <form class="container w-50" @submit.prevent="login">
      <h1>Log in</h1>
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
      <button type="submit" class="btn btn-primary m-3">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    login: function () {
      let userData = {
        email: this.email,
        password: this.password,
      };
      this.$store
        .dispatch("login", userData)
        .then(() => {
          this.$router.push("/dashboard");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style></style>
