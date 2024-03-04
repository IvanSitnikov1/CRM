<template>
    <section class="home-page">
        <div class="wrapper wrapper_title wrapper_small-margin">
            <Title
                class="home-page__welcome-title"
                :data="{
                    title: 'Welcome back, Evan!',
                    size: 'small',
                    isHighLeading: true,
                    marginBottom: 'small',
                }"
            />
        </div>
        <HeaderPage />
        <Workload />
        <Projects />
        <Events />
        <History />
    </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue';
import { Workload } from '@/widgets/workload';
import { History } from '@/widgets/history';
import { Projects } from '@/widgets/projects';
import { Events } from '@/widgets/events';
import { HeaderPage } from '@/entities/header-page';
import { Title } from '@/shared/ui/title';

useHead({
  title: 'CRM - Dashboard'
});

/* onBeforeUnmount(() => {
  bookModel.$reset()
}) */
</script>

<style lang="scss">
.home-page {
  &__welcome-title {
    color: #7D8592;
  }
}
.calendar-input {
  display: flex;
  column-gap: 16px;
  align-items: center;
  border-radius: 14px;
  background: #E6EDF5;
  padding: 12px 16px;
  &__date {
    color: #0A1629;
    font-size: 16px;
    font-weight: 400;
    line-height: 150%
  }
}
</style>
