<template>
  <article class="circle-progress">
    <svg
      class="circle-progress__svg"
      viewBox="-2 -2 108 108"
      :width="data.size"
      :height="data.size"
    >
      <circle
        class="circle-progress__circle circle-progress__line--back"
        :r="radius"
        cx="52"
        cy="52"
      />
      <circle
        class="circle-progress__circle circle-progress__line--top"
        :class="fillingCircleClasses"
        :style="fillingCircleStyles"
        :r="radius"
        cx="52"
        cy="52"
        transform="rotate(-270 52 52)"
      />
    </svg>

    <div class="circle-progress__content">
      <slot/>
    </div>
  </article>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue';
import type { ICircleProgressBar } from '@/shared/ui/circle-progress-bar'

const props = defineProps<{
  data: ICircleProgressBar
}>()


const isLimitReached = computed(() => props.data.max <= props.data.value);
const fillingCircleClasses = computed(() => {
  return {
    'circle-progress__line--filled': isLimitReached.value,
    'circle-progress__line--unfilled': !isLimitReached.value,
  };
});

const fillingCircleStyles = computed(() => {
  return {
    'strokeDashoffset': dashOffset.value,
    'strokeDasharray': dashArray.value,
  }
});

const currentFormatted = computed(() => isLimitReached.value ? props.data.max : props.data.value);

const radius = ref(48);
const dashArray = computed(() => radius.value * Math.PI * 2);
const dashOffset = computed(() => {
  return dashArray.value - dashArray.value * currentFormatted.value / props.data.max
});
</script>

<style lang="scss">
 @import "style.module";
</style>
