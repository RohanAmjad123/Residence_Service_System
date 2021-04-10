import { createRouter, createWebHashHistory } from "vue-router";
import Login from "@/views/Login";

const routes = [{ path: "/login", name: "Login", component: Login }, {}];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
