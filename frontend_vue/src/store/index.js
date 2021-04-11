import axios from "axios";
import { createStore } from "vuex";

export default createStore({
  state: {
    status: "",
    token: localStorage.getItem("token") || "",
    user: {},
  },
  mutations: {
    successfulLogin(state, token, user) {
      state.status = "success";
      state.token = token;
      state.user = user;
    },
    failedLogin(state) {
      state.status = "error";
    },
    logout(state) {
      state.status = "";
      state.token = "";
      state.user = "";
    },
  },
  actions: {
    login(context, userData) {
      return new Promise((resolve, reject) => {
        axios
          .post("token/", {
            email: userData.email,
            password: userData.password,
          })
          .then((response) => {
            const token = response.data.access;
            localStorage.setItem("token", token);
            context.commit("successfulLogin", token, userData);
            resolve(response);
          })
          .catch((error) => {
            console.log(error);
            context.commit("failedLogin");
            reject(error);
          });
      });
    },
    logout(context) {
      return new Promise((resolve, reject) => {
        context.commit("logout");
        localStorage.removeItem("token");
        axios.defaults.headers.common["Authorization"] = "";
        resolve();
        reject();
      });
    },
  },
  modules: {},
  getters: {
    isLoggedIn: (state) => !!state.token,
    authStatus: (state) => state.status,
  },
});
