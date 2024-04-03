<template>
    <div id="container">
    <div id="animation-area">
      <!-- 在这里放置你的CSS动画 -->
        <img src="../assets/login_background.jpg">
    </div>
    <div id="login-area">
        <div class="login-container">
        <h1>注册账户</h1>
        <form @submit.prevent="submitForm" class="register-form">
          <div class="form-group">
            <input type="text" id="username" v-model="form.username" required placeholder="用户名">
          </div>
          <div class="form-group">
            <input type="password" id="password" v-model="form.password" required placeholder="密码">
          </div>
          <div class="form-group">
            <input type="password" id="confirmPassword" v-model="form.confirmPassword" required placeholder="确认密码">
          </div>
          <div class="form-group">
            <input type="email" id="email" v-model="form.email" required placeholder="邮箱">
          </div>
          <button type="submit" class="submit-btn">注册</button>
        </form>
      </div>
    </div>
  </div>


  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'RegisterPage',
    data() {
      return {
        form: {
          username: '',
          password: '',
          confirmPassword: '',
          email: '',
        },
      };
    },
    methods: {
      async submitForm() {
        if (this.form.password !== this.form.confirmPassword) {
          alert('密码和确认密码不匹配！');
          return;
        }
        try {
          const response = await axios.post('http://127.0.0.1:8361/register', this.form);
          alert('注册成功！');
          console.log(response);
          // 重置表单或跳转到其他页面
        } catch (error) {
          console.error(error);
          alert('注册失败！');
        }
      },
    },
  };
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



  .register-page {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    background-color: #323B48; /* 主题色背景 */
    /* background-image: linear-gradient(135deg, #4A5568 25%, #323B48 25%, #323B48 50%, #4A5568 50%, #4A5568 75%, #323B48 75%, #323B48 100%); */
    background-size: 28.28px 28.28px; /* 图案大小 */
  }
  
  .register-container {
    padding: 40px;
    background: rgba(255, 255, 255, 0.9); /* 半透明白色背景 */
    border-radius: 8px; /* 圆角 */
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* 阴影效果 */
    width: 100%;
    max-width: 400px; /* 最大宽度，适应不同屏幕 */
  }
  
  h1 {
    color: #323B48;
    margin-bottom: 2rem; /* 增加距离 */
  }
  
  .form-group + .form-group {
    margin-top: 1rem;
  }
  
  input[type="text"],
  input[type="password"],
  input[type="email"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #CCC;
    border-radius: 4px;
    box-sizing: border-box;
  }
  
  .submit-btn {
    width: 100%;
    padding: 10px;
    background-color: #4A5568; /* 按钮颜色稍深 */
    color: white;
    border: none;
    border-radius: 4px;
    margin-top: 1rem;
    cursor: pointer;
  }
  
  .submit-btn:hover {
    background-color: #2D3748;
  }
  
  ::placeholder {
    color: #AAA;
  }
  </style>
  