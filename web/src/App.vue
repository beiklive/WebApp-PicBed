<template>
  <div id="app">
    <!-- <header> -->
      <!-- 头部内容，比如导航栏 -->
    <!-- </header> -->
    <!-- <main> -->
      <!-- 主体内容 -->
      <router-view />
      <!-- router-view组件用于展示当前路由匹配的组件 -->
    <!-- </main> -->
    <!-- <footer> -->
      <!-- 页脚内容 -->
    <!-- </footer> -->
  </div>
</template>

<script>
export default {
  name: 'App',
  // 可以在这里添加JavaScript逻辑，比如组件的数据、方法和生命周期钩子
}
</script>

<style>
/* 这里添加CSS样式 */
#app {
  text-align: center;
  height: 100%;
}



</style>
