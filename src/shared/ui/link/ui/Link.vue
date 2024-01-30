<template>
  <div class="link">
    <router-link
      class="link__text"
      :title="data.title"
      :to="data.to">
      {{ data.title }}
    </router-link >
    <img src="@/shared/assets/icons/arrowRight.svg" alt="arrow">
  </div>
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
