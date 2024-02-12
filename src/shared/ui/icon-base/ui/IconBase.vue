<template>
  <svg xmlns="http://www.w3.org/2000/svg"
       :width="24"
       :height="24"
       viewBox="0 0 24 24"
       :aria-labelledby="data.iconName"
       role="presentation"
  >
    <title
      :id="data.iconName"
      lang="en"
    >{{data.iconName}} icon</title>
    <g :fill="data.iconColor">
      <slot />
    </g>
  </svg>
</template>
<script setup lang="ts">
import { type IIcon } from './../index'

const props = defineProps<{
  data: IIcon
}>()


</script>

<style lang="scss">
 @import "style.module";
</style>
