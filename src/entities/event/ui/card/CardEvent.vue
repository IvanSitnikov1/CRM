<template>
  <article class="event">
    <div class="event__body">
      <div class="event__header">
        <Title class="event__name" :data="{
          title: data.title,
          isHighLeading: true,
          size: 'small',
        }"/>
        <Priority :data="{
          priority: data.priority
        }"/>
      </div>
      <div class="event__info">
        <time class="event__date">{{ data.day }} | {{ data.startTime }}</time>
         <TagTime :data="{
           time: data.time
         }"/>
      </div>
    </div>
  </article>
</template>

<script setup lang="ts">
import { Title } from '@/shared/ui/title'
import type { IEventCard } from "@/entities/event";
import IconBase from "@/shared/ui/icon-base/ui/IconBase.vue";
import { TagTime } from "@/shared/ui/tag-time";
import { Priority } from "@/shared/ui/priority";

const props = defineProps<{
  data: IEventCard
}>()

</script>

<style lang="scss">
 @import "style.module";
</style>
