<template>
  <section class="login" v-if="!isAuthenticated">
    <div class="login__logo">
      <img src="" alt="logo" class="login__image">
    </div>
    <main class="login__content">
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


const route = useRoute()


</script>

<style lang="scss">
  @import 'index.scss';
</style>
