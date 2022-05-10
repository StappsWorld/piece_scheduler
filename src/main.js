import { createApp } from "vue";
import App from "./App.vue";
import VCalendar from "v-calendar";

const app = createApp(App);
app.use(VCalendar, {});
app.mount("#app");
