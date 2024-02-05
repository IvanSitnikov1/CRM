<template>
  <section class="projects-page">
    <Header class="wrapper wrapper_title" :data="{
      title: 'Messenger'
    }"/>
    <div class="wrapper">
      <Collapse />
    </div>
  </section>
</template>

<script setup lang="ts">
import { Collapse } from '@/shared/ui/collaps'
import { Header } from '@/shared/ui/header'



</script>

<style lang="scss">
</style>
