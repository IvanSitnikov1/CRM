<template>
  <button class="button" :type="data.type">
    <img src="../../../assets/icons/support.svg" alt="Left Icon">
    <span class="button__text">
      {{ data.title }}
    </span>
  </button>
</template>

<script setup lang="ts">
import { type IButton } from './../index'

  const props = defineProps<{
    data: IButton
  }>()
</script>

<style lang="scss">
  @import "style.module";
</style>
