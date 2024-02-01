<template>
  <section class="calendar-page">
    <PopUp :data="{
        open: false,
        title: 'time',
      }">
      <template #content>
        <div class="date-selector">
          <TimePicker />
          <TimePicker />
        </div>
      </template>
    </PopUp>
    <Calendar />
  </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue'
import { TimePicker } from '@/shared/time-picker'
import { PopUp } from '@/entities/popup'
import { Calendar } from '@/widgets/calendar'

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
