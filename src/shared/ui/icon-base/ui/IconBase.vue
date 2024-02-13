<template>
  <svg xmlns="http://www.w3.org/2000/svg"
       :width="24"
       :height="24"
       viewBox="0 0 24 24"
       :aria-labelledby="data.iconName"
       role="presentation"
  >
    <title :id="data.iconName" lang="en">{{ data.iconName }} icon</title>
    <g :color="data.iconColor">
      <component :is="getIconComponent" />
    </g>
  </svg>
</template>

<script setup lang="ts">
import { defineAsyncComponent } from 'vue'
import type { IIcon } from "@/shared/ui/icon-base";

const props = defineProps<{
  data: IIcon;
}>();


const getIconComponent = defineAsyncComponent(() => {
    return import(`./../../../../shared/assets/icons/${props.data.iconName}.vue`);
})


</script>

<style lang="scss">
@import "style.module";
</style>
