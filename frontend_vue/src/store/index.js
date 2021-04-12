import axios from "axios";
import { createStore, createLogger } from "vuex";
import jwt_decode from "jwt-decode";

export default createStore({
  state: {
    status: "",
    token: localStorage.getItem("token") || "",
    user: {},
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
      
      if (decodedToken.is_student == true) {
        state.user.role = "student";
      } 
      else if (decodedToken.is_admin == true) {
        state.user.role = "admin";
      }
      else if (decodedToken.is_technician == true) {
        state.user.role = "technician";
      }
      else if (decodedToken.is_chef == true) {
        state.user.role = "chef";
      }
      else {
        state.user.role = "staff";
      }
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
  },
  plugins: process.env.NODE_ENV !== 'production'
    ? [createLogger()]
    : []
});
