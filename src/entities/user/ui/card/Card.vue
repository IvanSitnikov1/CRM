<template>
  <article
    class="employer-card"
    :class="{'employer-card_box': props.data.isBox}"
  >
    <div
      class="employer-card__about"
      :class="{'employer-card__about_white': props.data.isWhite}"
    >
      <CircleProgressBar
        class="employer-card__circle"
        :data="{
          size: 64,
          value: 23,
          max: 66,
        }"
      >
        <div class="employer-card__avatar">
          <img class="employer-card__image" :src="image" alt="avatar" />
        </div>
      </CircleProgressBar>
      <Title
        :data="{
          size: 'small',
          title: data.fullName
        }"
      />
      <div class="employer-card__job">
        {{ data.job }}
      </div>
      <Tag
        class="employer-card__tag"
        :data="{
          text: data.tag
        }"
      />
    </div>
    <div class="employer-card__add">
      <slot name="content"/>
    </div>
  </article>
</template>

<script setup lang="ts">
import { type IUserCard } from "src/entities/user";
import { CircleProgressBar } from '@/shared/ui/circle-progress-bar'
import { Title } from '@/shared/ui/title'
import { Tag } from '@/shared/ui/tag'

const props = defineProps<{
  data: IUserCard
}>()

const image = computed((): string | undefined => props.data?.image)
</script>

<style lang="scss">
@import "style.module";
</style>
