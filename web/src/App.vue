<template>
  <div id="container">
    <div id="animation-area">
      <!-- 在这里放置你的CSS动画 -->
      <div class="animation-example">动画展示区域</div>
    </div>
    <div id="login-area">
      <div class="login-container">
        <h1>登录</h1>
        <form @submit.prevent="login">
          <div class="form-group">
            <input type="email" id="email" v-model="email" placeholder="邮箱" required>
          </div>
          <div class="form-group">
            <input type="password" id="password" v-model="password" placeholder="密码" required>
          </div>
          <div class="form-group">
            <button type="submit">登录</button>
          </div>
        </form>
        <p class="register-prompt">还没有账号？<a href="#" @click.prevent="showRegister">注册</a></p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
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

<style>
#container {
  display: flex;
  height: 100vh;
}

#animation-area {
  flex: 4;
  background-color: #333;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
}

#login-area {
  flex: 2;
  background-color: #333;
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
  color: #333;
}

.form-group {
  margin-bottom: 20px;
}

.form-group input {
  width: 100%;
  padding: 15px;
  margin: 5px 0 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.form-group button {
  position: relative;
  width: 100%;
  padding: 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  justify-content: center;
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
