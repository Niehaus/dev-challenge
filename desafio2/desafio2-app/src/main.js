/* Imports Principais */
import { createApp } from 'vue'
import jquery from "jquery";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import App from './App.vue'
import router from './router/routes.js'

window.$ = window.jQuery = jquery;

/* Import de Estilos */
import "./assets/style/standards.sass"

/* Import de Componentes */
import Home from "./views/Home.vue";
import Sidebar from "./components/Sidebar.vue";
import Navbar from "./components/Navbar.vue";

/* Mount App */
const app = createApp(App)
app.component('Home', Home)
app.component('Sidebar', Sidebar)
app.component('Navbar', Navbar)

app.use(router).mount('#app')
