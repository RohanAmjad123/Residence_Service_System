import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

const token = localStorage.getItem("token");

axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:8000/api";
axios.defaults.headers.common["Authorization"] = "Bearer " + token;

createApp(App).use(store).use(router).mount("#app");
