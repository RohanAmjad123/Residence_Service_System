import { createRouter, createWebHashHistory } from "vue-router";
import store from "@/store/index";
import Login from "@/views/Login";
import Home from "@/views/Home";
import Dashboard from "@/views/Dashboard";
import MyComplaints from "@/views/Complaints/MyComplaints";
import MakeComplaint from "@/views/Complaints/MakeComplaint";
import MyMaintreqs from "@/views/Maintreqs/MyMaintreqs";
import MakeMaintreq from "@/views/Maintreqs/MakeMaintreq";
import MyFoodorders from "@/views/Foodorders/MyFoodorders";
import MakeFoodorder from "@/views/Foodorders/MakeFoodorder";
import MyPackages from "@/views/Packages/MyPackages";

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
    meta: { 
      requiresAuth: true, 
      roles: ["student", "staff", "admin", "technician", "chef"]
    },
  },
  {
    path: "/mycomplaints",
    name: "MyComplaints",
    component: MyComplaints,
    meta: { 
      requiresAuth: true,
      roles: ["student", "staff", "admin"]
    },
  },
  {
    path: "/make-complaint",
    name: "MakeComplaint",
    component: MakeComplaint,
    meta: { 
      requiresAuth: true,
      roles: ["student"]
    },
  },
  {
    path: "/mymaintreqs",
    name: "MyMaintreqs",
    component: MyMaintreqs,
    meta: { 
      requiresAuth: true,
      roles: ["student", "staff", "admin", "technician"]
    },
  },
  {
    path: "/make-maintreq",
    name: "MakeMaintreq",
    component: MakeMaintreq,
    meta: { 
      requiresAuth: true,
      roles: ["student"]
    },
  },
  {
    path: "/myfoodorders",
    name: "MyFoodorders",
    component: MyFoodorders,
    meta: { 
      requiresAuth: true,
      roles: ["student", "staff", "admin", "chef"]
    },
  },
  {
    path: "/make-foodorder",
    name: "MakeFoodorder",
    component: MakeFoodorder,
    meta: { 
      requiresAuth: true,
      roles: ["student"]
    },
  },
  {
    path: "/mypackages",
    name: "MyPackages",
    component: MyPackages,
    meta: { 
      requiresAuth: true,
      roles: ["student", "admin", "staff"]
    },
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      if (!to.meta.roles) {
        return next();
      }
      if (to.meta.roles.includes(store.state.role)) {
        return next();
      }
      return;
    }
    next("/login");
  } else {
    next();
  }
});

export default router;
