<template>
  <article class="checkbox">
    <div class="checkbox__title">
      {{ props.data.title }}
    </div>

    <div class="checkbox__group">
      <div v-for="(category, index) in props.data.categories" :key="index" class="checkbox__element">
        <label>
          <input type="checkbox" :name="checkboxGroupName" class="checkbox__element_real">
          <span class="checkbox__element_custom"></span>
          {{ category }}
        </label>
      </div>
    </div>
  </article>
</template>

<script setup lang="ts">
import type { ICheckbox } from '@/shared/ui/checkbox'

const props = defineProps<{
  data: ICheckbox
}>()

const checkboxGroupName = computed(() => {
  const id = "id" + Math.random().toString(16).slice(2)
  return `radio-group-${id}`;
});


</script>

<style lang="scss">
  @import "style.module";
</style>



