<template>
  <div class="link">
    <router-link
      class="link__text"
      :title="data.title"
      :to="data.to">
      {{ data.title }}
    </router-link >
  </div>
</template>

<script setup lang="ts">
import { type ILink } from './../index'

const props = defineProps<{
  data: ILink
}>()


</script>

<style lang="scss">
 @import "style.module";
</style>
