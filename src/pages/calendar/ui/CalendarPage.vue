<template>
  <section class="calendar-page">
    <Header class="wrapper wrapper_title" :data="{
      title: 'Dashboard'
    }"/>
    <Calendar />
  </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue'
import { Calendar } from '@/widgets/calendar'
import { Header } from '@/shared/ui/header'

useHead({
  title: 'Polka - Search book'
})


/*onBeforeUnmount(() => {
  bookModel.$reset()
})*/
</script>

<style scoped lang="scss">
.date-selector {
  perspective: 2000px;
  display: flex;
  border-radius: 24px;
  justify-content: space-between;
  max-width: 600px;
  width: 100%;
  .highlight {
    font-size: 20px;
  }
}
</style>
