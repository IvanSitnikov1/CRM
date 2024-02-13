<template>
  <article class="message">
    <div class="message__icon">
      <img class="message__image" src="@/shared/assets/test.png" alt="icon">
    </div>
    <div class="message__info">
      <Title :data="{
                    title: 'Medical App Team',
                    size: 'small',
                    isHighLeading: true
                  }"/>
      <div class="message__last">
        Caroline: Hi guys! I’ve share…
      </div>
    </div>
    <div class="message__data">
      <time class="message__time">12.04</time>
      <div class="message__not-read">
                    <span class="message__text-count">
                      12
                    </span>
      </div>
    </div>
  </article>
</template>

<script setup lang="ts">
import { type IBook } from 'src/entities/user'
import { Title } from '@/shared/ui/title'

const props = defineProps<{
  data: IBook
}>()
</script>

<style lang="scss">
 @import "style.module";
</style>
