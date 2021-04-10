import axios from "axios";
import { createStore } from "vuex";

export default createStore({
  state: {
    status: "",
    token: localStorage.getItem("token") || "",
    user: {},
  },
  mutations: {},
  actions: {
    login(context, userData) {
      axios
        .post("token/", { email: userData.email, password: userData.password })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  modules: {},
});
