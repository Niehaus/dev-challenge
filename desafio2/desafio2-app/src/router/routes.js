import { createWebHistory, createRouter } from "vue-router"

/* Main Route */
import Home from "../views/Home.vue";

/* Home Children - Subviews */
import DashboardView from "../views/DashboardView.vue";
import ProdView2 from "../views/ProdView2.vue";
import ClientView3 from "../views/ClientView3.vue";
import FornView4 from "../views/FornView4.vue";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
        children: [
            {
                path: 'home/dashboardview',
                component: DashboardView
            },
            {
                path: 'home/prodview',
                component: ProdView2
            },
            {
                path: 'home/clientview',
                component: ClientView3
            },
            {
                path: 'home/fornview',
                component: FornView4
            }
        ]
    }
]


const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;