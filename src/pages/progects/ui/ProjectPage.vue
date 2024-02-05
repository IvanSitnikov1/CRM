<template>
  <section class="projects-page">
    <PopUp :data="{
        open: true,
        title: 'time',
      }">
      <template #content>
        <div class="date-selector">
          <TimePicker
            :data="{
              source: generateHours(),
              count: 20,
              sensitivity: 0.8,
              value: currentHour
            }"
            @onChange="console.log($event)"
          />
          <TimePicker
            :data="{
              source: generateMinutes(),
              count: 20,
              sensitivity: 0.6,
              value: currentMinute
            }"
            @onChange="console.log($event)"
          />
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

const generateHours = () => new Array(23).fill(1).map((v, i) => {
  return { value: i + 1, text: i + 1}
});

const  generateMinutes = () => new Array(60).fill(1).map((v, i) => {
 return { value: i + 1, text: i + 1}
});

const currentHour = new Date().getHours();
const currentMinute = new Date().getMinutes();


/*onBeforeUnmount(() => {
  bookModel.$reset()
})*/
</script>

<style lang="scss">
.date-selector {
  perspective: 2000px;
  display: flex;
  border-radius: 24px;
  justify-content: space-between;
  max-width: 600px;
  width: 100%;
}
</style>
