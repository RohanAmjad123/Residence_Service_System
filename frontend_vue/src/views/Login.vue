<template>
  <div>
    <form class="login" @submit.prevent="login">
      <h1>Log in</h1>
      <div class="mb-3">
          <label class="form-label">Email</label>
          <input 
            required 
            v-model="email" 
            type="email" 
            placeholder="name@email.com"
            class="form-control" 
          />
          <label>Password</label>
          <input
            required
            v-model="password"
            type="password"
            placeholder="password"
            class="form-control"
          />
          <button type="submit" class="btn btn-primary">Login</button>
      </div>
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

<style>
</style>
