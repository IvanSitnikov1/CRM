<template>
  <article class="employer-card" v-for="index in 2" :key="index">
    <div class="employer-card__avatar">
      <img class="employer-card__image" :src="image" alt="avatar">
    </div>
    <div class="header header_size-small">
      Shawn Stone
    </div>
    <div class="employer-card__job">
      UI/UX Designer
    </div>
    <div class="tag">
      Middle
    </div>
  </article>
</template>

<script setup lang="ts">
import { type IBook } from 'src/entities/user'

const props = defineProps<{
  data: IBook
}>()

const image = computed((): string | undefined => props.data?.image)

const href = computed((): string => `/book/${props.data.id}`)
</script>

<style lang="scss">
  @import "style.module";
</style>
