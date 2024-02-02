<template>
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
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'
import { useScroll } from '@vueuse/core'
import { Panel } from '@/widgets/panel'
import { Navigation } from '@/widgets/navigation'
import { FabBottomSheet } from '@/widgets/fab'
import { ActionPlus } from '@/features/action-plus'
import { PopUp } from '@/entities/popup'
import { Support } from '@/widgets/support'

const route = useRoute()


const { arrivedState } = useScroll(document, { behavior: 'smooth' })
const layout = computed(() => route.meta.layout || DefaultLayout)
</script>

<style lang="scss">
  @import 'index.scss';
</style>
