<template>
  <section class="calendar-page">
    <div class="wrapper">
      <DataPiker data=""/>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue'
import { DataPiker } from '@/shared/ui/data-picker'

useHead({
  title: 'Polka - Search book'
})


/*onBeforeUnmount(() => {
  bookModel.$reset()
})*/
</script>

<style scoped lang="scss">
</style>
