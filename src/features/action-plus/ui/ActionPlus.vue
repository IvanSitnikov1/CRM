<template>
  <article class="actions" @click="app.updateShowFab(true)">
    <span class="actions__plus">+</span>
  </article>
</template>

<script setup lang="ts">
import { useAppModel } from '@/entities/app'

const app = useAppModel()

</script>

<style lang="scss">
  @import "style.module";
</style>

