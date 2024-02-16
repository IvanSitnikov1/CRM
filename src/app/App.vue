<template>
  <section class="no-auth" v-if="!isAuthenticated">
    <div class="wrapper">
      <aside class="no-auth__header">
        <div class="no-auth__logo">
          <img src="@/shared/assets/specialIcons/logo.svg" alt="logo" class="login__image">
        </div>
        <span class="no-auth__title">CRM</span>
      </aside>
    </div>
    <main class="no-auth__content">
      <router-view v-slot="{ Component }">
        <transition name="page" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
  </section>
  <section class="app" v-else>
    <Panel />
    <main>
      <router-view v-slot="{ Component }">
        <transition name="page" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
    <ActionPlus />
    <Navigation />
    <FabBottomSheet />
    <Support />
    <AddEmployee />
  </section>

</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'
import { Panel } from '@/widgets/panel'
import { Navigation } from '@/widgets/navigation'
import { FabBottomSheet } from '@/widgets/fab'
import { ActionPlus } from '@/features/action-plus'
import { Support } from '@/widgets/support'
import { isAuthenticated } from "@/shared/lib/ustils/isAutorise";
import { AddEmployee } from "@/widgets/add-employee";


const route = useRoute()


</script>

<style lang="scss">
  @import 'index.scss';

  .no-auth {
    margin-top: 56px;
    &__header {
      display: flex;
      align-items: center;
      column-gap: 16px;
      justify-content: center;
    }
    &__title {
      color: rgb(58, 137, 255);
      font-size: 20px;
      font-weight: 700;
      line-height: 150%;
    }
  }
</style>
