<template>
  <article class="title-with-link" :class="data.class">
    <Title :data="{
      marginBottom: 'none',
      title: data.title?.title,
      isHighLeading: data.title?.isHighLeading,
      size: 'large'
    }"/>
    <div class="title-with-link__link">
      <Link :data="data.link"/>
      <IconBase :data="{
        iconName: 'arrow'
      }">
        <ArrowRightIcon />
      </IconBase>
    </div>

  </article>
  <slot name="content"/>
</template>

<script setup lang="ts">
import { type ITitleWithLink } from 'src/entities/grop-title'
import Link from '@/shared/ui/link/ui/Link.vue'
import { Title } from '@/shared/ui/title'
import IconBase from "@/shared/ui/icon-base/ui/IconBase.vue";
import ArrowRightIcon from "@/shared/assets/icons/arrowRight.vue";

const props = defineProps<{
  data: ITitleWithLink
}>()

</script>

<style lang="scss">
 @import "style.module";
</style>
