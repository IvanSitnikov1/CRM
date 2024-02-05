<template>
  <button @click="isExpanded = !isExpanded">Trigger</button>

  <Collapse :when="isExpanded">
    <p>{{ 'Collapsed '.repeat(100) }}</p>
  </Collapse>
</template>

<script setup>
import { Collapse } from 'vue-collapsed'

const isExpanded = ref(false)
</script>

<style lang="scss">
 @import "styles.module";
</style>
