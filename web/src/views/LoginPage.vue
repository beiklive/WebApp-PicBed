<template>
  <div id="container">
    <div id="animation-area">
      <!-- 在这里放置你的CSS动画 -->
        <img src="../assets/login_background.jpg">
    </div>
    <div id="login-area">
      <div class="login-container">
        <h1>登录</h1>
        <form @submit.prevent="login">
          <div class="form-group">
            <input type="email" id="email" v-model="email" placeholder="用户名/邮箱" required>
          </div>
          <div class="form-group">
            <input type="password" id="password" v-model="password" placeholder="密码" required>
          </div>
          <div class="form-group">
            <button type="submit">登录</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    login() {
      alert(`登录功能尚未实现。`);
    },
    showRegister() {
      alert(`注册功能尚未实现。`);
    }
  }
}
</script>

<style scoped>
#container {
  display: flex;
  height: 100vh;
  color: white;
}

#animation-area {
  
  flex: 4;
  background-color: #333;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  z-index: -1;
  overflow: hidden;
}

#animation-area img {
  width: fit-content;
  height: 100%;
  padding-left: 10%;
}

#login-area {
  flex: 2;
  background-color: #323B48;
  display: flex;
  justify-content: center;
  color: white;
  align-items: center;
}

.login-container {
  width: 300px;
}

.login-container h1 {
  text-align: center;
  color: white;
}

.form-group {
  margin-bottom: 20px;
}

.form-group input {
  width: 100%;
  padding: 10px;
  margin: 5px 0 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

.form-group button {
  width: 100%;
    padding: 10px;
    background-color: #4A5568; /* 按钮颜色稍深 */
    color: white;
    border: none;
    border-radius: 4px;
    margin-top: 1rem;
    cursor: pointer;
}

.form-group button:hover {
  background-color: #0056b3;
}

.register-prompt {
  text-align: center;
}

.register-prompt a {
  color: #007bff;
  text-decoration: none;
}
</style>
