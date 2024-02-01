<template>
  <section class="calendar-page">
    <div class="wrapper">
      <DataPiker :data="{}"/>
      <TimePicker />
    </div>
  </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue'
import { DataPiker } from '@/shared/ui/data-picker'
import { UiSelect } from 'src/shared/time-picker'
import { TimePicker } from '@/shared/time-picker'

useHead({
  title: 'Polka - Search book'
})


/*onBeforeUnmount(() => {
  bookModel.$reset()
})*/
</script>

<style scoped lang="scss">
</style>
