import { createRouter, createWebHashHistory } from "vue-router";
import store from "@/store/index";
import Login from "@/views/Login";
import Home from "@/views/Home";
import Dashboard from "@/views/Dashboard";
import MyComplaints from "@/views/Complaints/MyComplaints";
import MakeComplaint from "@/views/Complaints/MakeComplaint";

const routes = [
  { 
    path: "/login", 
    name: "Login", 
    component: Login 
  },
  { 
    path: "/home", 
    name: "Home", 
    component: Home 
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    meta: { requiresAuth: true },
  },
  {
    path: "/mycomplaints",
    name: "MyComplaints",
    component: MyComplaints,
    meta: { requiresAuth: true },
  },
  {
    path: "/make-complaint",
    name: "MakeComplaint",
    component: MakeComplaint,
    meta: { requiresAuth: true },
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      next();
      return;
    }
    next("/login");
  } else {
    next();
  }
});

export default router;
