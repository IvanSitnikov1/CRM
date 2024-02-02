<template>
  <section class="projects-page">
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
    <Header class="wrapper wrapper_title" :data="{
      title: 'Projects'
    }"/>
  </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue'
import { TimePicker } from '@/shared/ui/time-picker'
import { PopUp } from '@/entities/popup'
import { Header } from '@/shared/ui/header'

useHead({
  title: 'Projects'
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
