import { createRouter, createWebHashHistory } from "vue-router";
import Login from "@/views/Login";
import Home from "@/views/Home"

const routes = [
  { path: "/login", name: "Login", component: Login }, 
  { path: "/home", name: "Home", component: Home},
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
