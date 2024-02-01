<template>
  <section class="calendar-page">
    <div class="wrapper">
      <DataPiker :data="{}"/>
      <PopUp :data="{
        open: true,
        title: 'time',
      }">
        <template #content>
          <div class="date-selector">
            <TimePicker />
            <TimePicker />
          </div>
        </template>
      </PopUp>

    </div>
  </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue'
import { DataPiker } from '@/shared/ui/data-picker'
import { UiSelect } from 'src/shared/time-picker'
import { TimePicker } from '@/shared/time-picker'
import { PopUp } from '@/entities/popup'

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
