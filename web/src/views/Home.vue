<template>
  <div class="home">
    <h1>Welcome to the Home Page</h1>
    <p>This is the main page of our Vue application.</p>
    <router-link to="/login">Login</router-link>
    <router-link to="/register">Register</router-link>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  // 在这里可以添加更多的组件逻辑，如数据(properties), 计算属性(computed properties), 方法(methods)等。
}
</script>

<style scoped>
/* 使用scoped属性使样式仅应用于此组件 */
.home {
  padding: 20px;
  text-align: center;
}

h1 {
  color: #42b983;
}

p {
  margin: 20px 0;
  color: #35495e;
}
</style>
