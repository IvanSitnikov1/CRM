<template>
  <section class="events-page">
    <div class="wrapper wrapper_title events-page__back">
      <Link :data="{
        title: 'Back to Dashboard',
        to: '/',
        iconLeft: 'arrowLeftLong'
      }">

      </Link>
    </div>
    <Title class="wrapper wrapper_title" :data="{
      title: 'Projects'
    }"/>
    <div class="wrapper">
      <div class="events-page__events">
        <CardEvent
          v-for="index in 7"
          :key="index"
          :data="{
            day: 'Today',
            startTime: '5:00 PM',
            title: 'Meeting with Development Team',
            time: '4h',
            priority: 'medium'
          }"
        />
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue'
import { TimePicker } from '@/shared/ui/time-picker'
import { PopUp } from '@/entities/popup'
import { Header } from '@/shared/ui/header'
import { Title } from "@/shared/ui/title";
import CardEvent from "@/entities/event/ui/card/CardEvent.vue";
import Link from "@/shared/ui/link/ui/Link.vue";

useHead({
  title: 'Projects'
})

/*onBeforeUnmount(() => {
  bookModel.$reset()
})*/
</script>

<style lang="scss">
.events-page {
  &__events {
    display: flex;
    flex-direction: column;
    row-gap: 20px;
  }
}
</style>
