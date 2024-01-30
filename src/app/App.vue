<template>
  <Panel />
  <main>
    <transition name="page">
      <router-view />
    </transition>
  </main>
  <ActionPlus />
  <Navigation />
  <FabBottomSheet />
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'
import { useScroll } from '@vueuse/core'
import { Panel } from '@/widgets/panel'
import { Navigation } from '@/widgets/navigation'
import { FabBottomSheet } from '@/widgets/fab'
import { ActionPlus } from '@/features/action-plus'

const route = useRoute()


const { arrivedState } = useScroll(document, { behavior: 'smooth' })
const layout = computed(() => route.meta.layout || DefaultLayout)
</script>

<style lang="scss">
  @import 'index.scss';
</style>
