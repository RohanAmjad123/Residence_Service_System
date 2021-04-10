import { createRouter, createWebHashHistory } from "vue-router";
import Login from "@/views/Login";
import Home from "@/views/Home"
import Dashboard from "@/views/Dashboard"

const routes = [
  { path: "/login", name: "Login", component: Login }, 
  { path: "/home", name: "Home", component: Home},
  { path: "/dashboard", name: "Dashboard", component: Dashboard}
  
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
