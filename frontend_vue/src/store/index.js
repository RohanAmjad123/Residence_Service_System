import axios from "axios";
import { createStore, createLogger } from "vuex";
import jwt_decode from "jwt-decode";
import createPersistedState from "vuex-persistedstate";

export default createStore({
  state: {
    status: "",
    token: localStorage.getItem("token") || "",
    user: {},
    role: ""
  },
  mutations: {
    successfulLogin(state, token) {
      state.status = "success";
      state.token = token;
      let decodedToken = jwt_decode(token);
      state.user = {};
      state.user.user_id = decodedToken.user_id;
      state.user.email = decodedToken.email;
      state.user.first_name = decodedToken.first_name;
      state.user.last_name = decodedToken.last_name;

      let role = "";
      if (decodedToken.is_student == true) {
        role = "student"
      } 
      else if (decodedToken.is_admin == true) {
        role = "admin";
      }
      else if (decodedToken.is_technician == true) {
        role = "technician";
      }
      else if (decodedToken.is_chef == true) {
        role = "chef";
      }
      else {
        role = "staff";
      }
      state.role = role;
    },
    failedLogin(state) {
      state.status = "error";
    },
    logout(state) {
      state.status = "";
      state.token = "";
      state.role = "";
      state.user = "";
      localStorage.removeItem("token");
      localStorage.removeItem("role")
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
            context.commit("successfulLogin", token);
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
    getRole: (state) => state.role,
    getUserID: (state) => {
      return state.user.user_id;
    }
  },
  plugins: process.env.NODE_ENV !== 'production'
    ? [createLogger(), createPersistedState()]
    : []
});
