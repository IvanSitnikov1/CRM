<template>
  <article class="radio">
    <div class="radio__title">
      {{ props.data.title }}
    </div>

    <div class="radio__group">
      <div v-for="(category, index) in props.data.categories" :key="index" class="radio__element">
        <label>
          <input type="radio" :name="radioGroupName" :value="category" class="radio__element_real">
          <span class="radio__element_custom"></span>
          {{ category }}
        </label>
      </div>
    </div>
  </article>
</template>

<script setup lang="ts">
import type { IRadio } from '@/shared/ui/radio'


const props = defineProps<{
  data: IRadio
}>()

const radioGroupName = computed(() => {
  const id = "id" + Math.random().toString(16).slice(2)
  return `radio-group-${id}`;
});


</script>

<style lang="scss">
@import "style.module";
</style>



