<template>
  <article class="title-with-link" :class="data.class">
    <Title :data="{
      marginBottom: 'none',
      title: data.title?.title,
      isHighLeading: data.title?.isHighLeading,
      size: 'large'
    }"/>
    <div class="title-with-link__link">
      <Link :data="{
        iconRight: 'arrowRight',
        iconRightColor: '#3F8CFF',
        title: data.link?.title,
        to: data.link?.to || '/'
      }"/>
    </div>
  </article>
  <slot name="content"/>
</template>

<script setup lang="ts">
import { type ITitleWithLink } from 'src/entities/grop-title'

import { Title } from '@/shared/ui/title'
import Link from "@/shared/ui/link/ui/Link.vue";

const props = defineProps<{
  data: ITitleWithLink
}>()

</script>

<style lang="scss">
 @import "style.module";
</style>
