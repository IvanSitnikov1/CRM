<template>
  <article class="info-panel__logo" @click="app.toggleShowMenu()">
    <img src="./../../../shared/assets/specialIcons/logo.svg" alt="logo">
  </article>
</template>

<script setup lang="ts">
import { useAppModel } from '@/entities/app'

const app = useAppModel()

</script>
