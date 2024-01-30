<template>
  <div :class="classes">
    {{ data.title}}
  </div>
</template>

<script setup lang="ts">
import { type ITitle } from '../../title'

const props = defineProps<{
  data: ITitle
}>()

const classes = computed(() => {
  const temp = [];
  temp.push('title')
  switch (props.data.size) {
    case 'medium':
      temp.push('title_size-medium')
      break;
    case 'small':
      temp.push('title_size-small')
      break;
  }
  switch (props.data.marginBottom) {
    case 'large':
      temp.push('title_margin-large')
      break;
    case 'medium':
      temp.push('title_margin-medium')
      break;
    case 'small':
      temp.push('title_margin-small')
      break;
  }
  if (props.data.isHighLeading) {
    temp.push('title_line-height')
  }
  return temp;
})

</script>

<style lang="scss">
  @import "style.module";
</style>



