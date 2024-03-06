<template>
    <section class="project-detail-page">
        <BackLink />
        <Task />
    </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue';
import { Task } from '@/widgets/task';
import { BackLink } from '@/entities/back-link'

useHead({
  title: 'Project details'
});

</script>

<style lang="scss">
.project-detail-page {
  &__description {
    margin-bottom: 52px;
  }
}
</style>
