<template>
    <section class="project-detail-page">
        <BackLink />
        <Task />
        <Task />
        <History />
    </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue';
import { History } from '@/widgets/history';
import { Task } from '@/widgets/task';
import { BackLink } from '@/entities/back-link';

useHead({
  title: 'Project details'
});

</script>
