<template>
    <section class="events-page">
        <BackLink />
        <Title
            class="wrapper wrapper_title"
            :data="{
                title: 'Projects',
            }"
        />
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
                        priority: 'medium',
                    }"
                />
            </div>
        </div>
    </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue';
import { Title } from '@/shared/ui/title';
import { BackLink } from '@/entities/back-link';
import { CardEvent } from '@/entities/event'

useHead({
  title: 'CRM - Nears event'
});

/* onBeforeUnmount(() => {
  bookModel.$reset()
}) */
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
