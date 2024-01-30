<template>
  <section class="calendar-page">
    <div class="wrapper">
      <UICalendar data=""/>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue'
import { UICalendar } from '@/shared/ui/calendar'

useHead({
  title: 'Polka - Search book'
})


/*onBeforeUnmount(() => {
  bookModel.$reset()
})*/
</script>

<style scoped lang="scss">
</style>
