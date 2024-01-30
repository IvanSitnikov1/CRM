<template>
  <button class="button">
    <img src="../../../assets/icons/support.svg" alt="Left Icon">
    <span class="button__text">
      {{ data.title }}
    </span>
  </button>
</template>

<script setup lang="ts">
import { type ILink } from '../../link'

  const props = defineProps<{
    data: ILink
  }>()
</script>

<style lang="scss">
  @import "style.module";
</style>
