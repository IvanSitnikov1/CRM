<template>
  <section class="calendar-page">
    <HeaderPage />
    <Calendar />
  </section>
</template>

<script setup lang="ts">
import { useHead } from '@unhead/vue'
import { Calendar } from '@/widgets/calendar'
import { HeaderPage } from '@/entities/header-page'

useHead({
  title: 'CRM - Calendar'
})

</script>
