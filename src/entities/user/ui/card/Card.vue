<template>
  <article class="employer-card"
           :class="{'employer-card_box': props.data.isBox}"
  >
    <div class="employer-card__about">
      <CircleProgressBar class="employer-card__circle" :data="{
      size: 64,
      value: 23,
      max: 66,
    }">
        <div class="employer-card__avatar" >
          <img class="employer-card__image" :src="image" alt="avatar">
        </div>
      </CircleProgressBar>
      <Title :data="{
      size: 'small',
      title: 'Shawn Stone'
    }"/>
      <div class="employer-card__job">
        UI/UX Designer
      </div>
      <Tag class="employer-card__tag" :data="{
      text: 'Middle'
    }"/>
    </div>
    <div class="employer-card__add">
      <slot name="content">

      </slot>
    </div>
  </article>
</template>

<script setup lang="ts">
import { type IBook } from 'src/entities/user'
import { CircleProgressBar } from '@/shared/ui/circle-progress-bar'
import { Title } from '@/shared/ui/title'
import { Tag } from '@/shared/ui/tag'

const props = defineProps<{
  data: IBook
}>()

const image = computed((): string | undefined => props.data?.image)

const href = computed((): string => `/book/${props.data.id}`)
</script>

<style lang="scss">
  @import "style.module";
</style>
