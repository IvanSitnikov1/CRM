<template>
  <article class="title-with-link" :class="data.class">
    <Title :data="{
      marginBottom: 'none',
      title: data.title?.title,
      isHighLeading: data.title?.isHighLeading,
      size: 'large'
    }"/>

    <Link :data="data.link"/>
  </article>
  <slot name="content"/>
</template>

<script setup lang="ts">
import { type ITitleWithLink } from 'src/entities/grop-title'
import Link from '@/shared/ui/link/ui/Link.vue'
import { Title } from '@/shared/ui/title'

const props = defineProps<{
  data: ITitleWithLink
}>()

</script>

<style lang="scss">
 @import "style.module";
</style>
