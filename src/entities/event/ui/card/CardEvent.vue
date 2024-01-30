<template>
  <article class="event" v-for="index in 7" :key="index">
    <div class="event__body">
      <div class="event__header">
        <Title class="event__name" :data="{
          title: 'Presentation of the new department',
          isHighLeading: true,
          size: 'small',
        }"/>
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
          <path d="M12.6129 4.2097L12.7071 4.29289L17.7071 9.29289C18.0976 9.68342 18.0976 10.3166 17.7071 10.7071C17.3466 11.0676 16.7794 11.0953 16.3871 10.7903L16.2929 10.7071L13 7.415V19C13 19.5523 12.5523 20 12 20C11.4872 20 11.0645 19.614 11.0067 19.1166L11 19V7.415L7.70711 10.7071C7.34662 11.0676 6.77939 11.0953 6.3871 10.7903L6.29289 10.7071C5.93241 10.3466 5.90468 9.77939 6.2097 9.3871L6.29289 9.29289L11.2929 4.29289C11.6534 3.93241 12.2206 3.90468 12.6129 4.2097Z" fill="#FFBD21"/>
        </svg>
      </div>
      <div class="event__info">
        <time class="event__date">Today | 5:00 PM</time>
        <div class="tag-time">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M12 20C16.4183 20 20 16.4183 20 12C20 7.58172 16.4183 4 12 4C7.58172 4 4 7.58172 4 12C4 16.4183 7.58172 20 12 20ZM12.9933 8.88338C12.9355 8.38604 12.5128 8 12 8C11.4477 8 11 8.44772 11 9V12.75L11.0072 12.8698C11.0498 13.2244 11.28 13.5333 11.6154 13.6731L14.6154 14.9231L14.7256 14.9617C15.2069 15.0997 15.7258 14.858 15.9231 14.3846L15.9617 14.2744C16.0997 13.7931 15.858 13.2742 15.3846 13.0769L13 12.083V9L12.9933 8.88338Z" fill="#7D8592"/>
          </svg>
          <time class="event__date">4h</time>
        </div>
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
