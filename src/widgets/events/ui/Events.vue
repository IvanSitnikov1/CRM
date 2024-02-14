<template>
  <div class="wrapper_big-margin">
    <section class="event-container">
      <TitleWithLink :data="{
        title: {
          title: 'Events'
        },
        link: {
          title: 'View all',
          to: '/nears-events'
        },
        class: 'wrapper events__title'
      }">
        <template #content>
          <section class="events">
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
          </section>
        </template>
      </TitleWithLink>
    </section>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { TitleWithLink } from '@/entities/grop-title'
import CardEvent from '@/entities/event/ui/card/CardEvent.vue'

const router = useRouter()
const goToHome = () => {
  router.push({ path: '/' })
}

</script>


<style lang="scss">
  @import "style.module";
</style>
