<template>
  <section class="not-found">
    <img src="./../../../shared/assets/specialIcons/nofFound.svg" alt="Not Found">
    <h2>{{ title }}</h2>
  </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue'

const title = computed((): string => '404 - page not found')

useHead({
  title: title.value
})
</script>

<style lang="scss" scoped>
.not-found {
  text-align: center;
}
</style>
