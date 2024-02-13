<template>
  <section class="events-page">
    <div class="wrapper wrapper_title events-page__back">
      <Link :data="{
        title: 'Back to Dashboard',
        to: '/'
      }">

      </Link>
    </div>
    <Title class="wrapper wrapper_title" :data="{
      title: 'Projects'
    }"/>
    <div class="wrapper">
      <div class="events-page__events">
        <CardEvent data=""/>
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
