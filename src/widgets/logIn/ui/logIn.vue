<template>
  <div class="wrapper">
    <section class="login">
        <Title class="login__title" :data="{
          title: 'Sign In to CRM',
          size: 'medium',
          isHighLeading: true,
          marginBottom: 'medium'
        }"/>
        <form class="login__form" @submit.prevent="submitForm">
          <UIInput class="login__email"
                   @onInput="handlerEmail"
                   :data="{
                      title: 'Email Address',
                      name: 'email',
                      type: 'email',
                      placeholder: 'youremail@gmail.com',
                      value: state.fromData.email
                   }"/>
          <UIInput class="login__password"
                   @onInput="handlerPassword"
                   :data="{
                      title: 'Password',
                      name: 'password',
                      type: 'password',
                      placeholder: '••••••••',
                      value: state.fromData.password,
                      iconName: 'eye'
                    }">
            <template #icon>
              <arrow-right-long-icon/>
            </template>
          </UIInput>
          <div class="login__action">
            <button class="login__reset" type="reset">
              Reset All Field
            </button>

            <router-link to="/forgot" class="login__forgot">
                Forgot Password?
            </router-link>
          </div>
          <UiButton class="login__button" :data="{
            title: 'Sign In',
            type: 'submit',
            iconNameRight: 'Arrow Right',
            isFull: true
          }">
            <template #icon-right>
              <arrow-right-long-icon/>
            </template>
          </UiButton>
          <Link @click="handlerCreateUser" class="login__link" :data="{
            title: 'Don’t have an account?',
            to: '/'
          }"/>
        </form>
    </section>
  </div>
  <PopUp :data="{
    title: 'Allow notification?',
    open: isSupported
  }">
    <template #content>
      <div class="login__pop-up">
        <UiButton class="login__choise"
                  :data="{
                    type: 'button',
                    title: 'Yes'
                  }"/>
        <UiButton class="login__choise"
                  :data="{
                     type: 'button',
                     title: 'No'
                   }"/>
      </div>

    </template>

  </PopUp>
</template>

<script setup lang="ts">

import { router } from "@/app/providers";
import { http } from "@/shared/api";
import { Title } from "@/shared/ui/title";
import { UIInput } from "@/shared/ui/input";
import { UiButton } from "@/shared/ui/button";
import Link from "@/shared/ui/link/ui/Link.vue";
import ArrowRightLongIcon from "@/shared/assets/icons/arrowRightLong.vue";
import { accessTokenLocalStorage, refreshTokenLocalStorage } from "@/shared/lib/ustils/isAutorise";
import { useCustomWebNotification } from "@/shared/lib/ustils/notification";
import { PopUp } from "@/entities/popup";

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
    const refreshToken = response.data.refreshToken;
    accessTokenLocalStorage.value = accessToken
    refreshTokenLocalStorage.value = refreshToken
    await router.push({ path: '/' })
  } catch (error) {
    console.error('Error submitting form:', error);
  }
};

const { isSupported, show: showNotification } = useCustomWebNotification();

const handlerCreateUser = () => {
  accessTokenLocalStorage.value = 'test user'
  refreshTokenLocalStorage.value = 'test token'
  if (isSupported.value) {
    // Customize and show the notification
    showNotification({
      title: 'Custom Notification',
      body: 'Create Test User!',
    });
  }

  router.push({ path: '/' })
}

const handlerEmail = (event: string) => {
  state.fromData.email = event
}

const handlerPassword = (event: string) => {
  state.fromData.password = event
}
</script>


<style scoped lang="scss">
  @import "style.module";
</style>
