<template>
  <article class="tag">
    {{ data.text }}
  </article>
</template>

<script setup lang="ts">
import { type ITag } from './../index'

const props = defineProps<{
  data: ITag
}>()

</script>

<style lang="scss">
 @import "styles.module";
</style>
