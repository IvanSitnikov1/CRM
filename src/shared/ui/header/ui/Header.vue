<template>
  <h1 class="header">
    {{ data.title}}
  </h1>
</template>

<script setup lang="ts">
import { type IHeader } from './../index'

const props = defineProps<{
  data: IHeader
}>()

</script>

<style lang="scss">
  @import "style.module";
</style>



