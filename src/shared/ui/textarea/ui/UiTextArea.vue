<template>
  <article class="textarea">
    <label :for="data.name" class="label textarea__label">
      {{ data.title}}
    </label>
    <textarea
      class="textarea__text"
      :name="data.name"
      :id="data.name"
      :placeholder="data.placeholder"
      rows="4"/>
  </article>
</template>

<script setup lang="ts">
import { type ITextArea } from './../index'

const props = defineProps<{
  data: ITextArea
}>()
</script>

<style lang="scss">
  @import "style.module";
</style>



