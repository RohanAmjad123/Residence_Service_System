<template>
    <div>
        <form class="login" @submit.prevent="login">
            <h1>Log in</h1>
            <label>Email</label>
            <input required v-model="email" type="email" placeholder="Email"/>
            <label>Password</label>
            <input required v-model="password" type="password" placeholder="Password"/>
            <button type="submit">Login</button>
        </form>
    </div>
</template>

<script>
export default {
    components: {},
    data () {
        return {
            email: '',
            password: ''
        }
    },
    methods: {
      login: function () {
        let userData = {
            email: this.email,
            password: this.password
        }
        this.$store.dispatch('login', userData)
      }
    }
}
</script>