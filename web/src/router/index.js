import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import LoginPage from '../views/LoginPage.vue';
import Register from '../views/Register.vue';

// 定义路由
// 每个路由应该映射到一个组件。其中"component"可以是
// 通过Vue.extend()创建的组件构造器，
// 或者，只是一个组件配置对象。
const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: Home
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: LoginPage
  },
  {
    path: '/register', // 注册页面路由
    name: 'RegisterPage',
    component: Register
  }
];

// 创建路由实例并传递`routes`配置
// 你可以在这里传递不同的路由配置参数
const router = createRouter({
  // 采用HTML5模式
  history: createWebHistory(process.env.BASE_URL),
  routes // (缩写) 相当于 routes: routes
});

export default router;
