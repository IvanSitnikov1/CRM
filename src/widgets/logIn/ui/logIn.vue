<template>
  <div class="wrapper">
    <section class="screen">
      <div class="screen__content">
        <form class="login" @submit.prevent="submitForm">
          <div class="login__field">
            <i class="login__icon fas fa-user"></i>
            <input type="text" class="login__input" v-model="state.fromData.email" name="email" placeholder="User name / Email">
          </div>
          <div class="login__field">
            <i class="login__icon fas fa-lock"></i>
            <input type="password" class="login__input" v-model="state.fromData.password"  name="password" placeholder="Password">
          </div>
          <button class="button login__submit">
            <span class="button__text">Log In Now</span>
            <i class="button__icon fas fa-chevron-right"></i>
          </button>
        </form>
        <div class="social-login">
          <h3>log in via</h3>
          <div class="social-icons">
            <a href="#" class="social-login__icon fab fa-instagram"></a>
            <a href="#" class="social-login__icon fab fa-facebook"></a>
            <a href="#" class="social-login__icon fab fa-twitter"></a>
          </div>
        </div>
      </div>
      <div class="screen__background">
        <span class="screen__background__shape screen__background__shape4"></span>
        <span class="screen__background__shape screen__background__shape3"></span>
        <span class="screen__background__shape screen__background__shape2"></span>
        <span class="screen__background__shape screen__background__shape1"></span>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">

import { router } from "@/app/providers";
import { http } from "@/shared/api";

const state = reactive({
  fromData: {
    email: '',
    password: '',
    agent: navigator.userAgent
  }
})
const submitForm = async () => {
  try {
    const response = await http.post('http://localhost:3000/auth/logIn', state.fromData);
    const accessToken = response.data.accessToken;
    localStorage.setItem('token', accessToken);
    await router.push({ path: '/' })
  } catch (error) {
    console.error('Error submitting form:', error);
  }
};
</script>


<style scoped lang="scss">
  @import "style.module";
</style>
