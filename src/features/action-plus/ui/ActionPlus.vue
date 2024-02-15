<template>
    <article
        class="actions"
        @click="handlerOpenAddModal($route.path)"
    >
        <span class="actions__plus">+</span>
    </article>
</template>

<script setup lang="ts">
import { useAppModel } from '@/entities/app';

const app = useAppModel();

const handlerOpenAddModal = path => {
  switch (path) {
    case '/':
      app.updateShowFab(true);
      break;
    default:
      console.log('Пока не готов');
  }
};
</script>

<style lang="scss">
  @import "style.module";
</style>
