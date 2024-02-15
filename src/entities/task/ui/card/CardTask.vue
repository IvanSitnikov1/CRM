<template>
  <article class="task">
    <div class="task__header">
      <div class="task__meta">
        <div class="task__index">
          Task Name
        </div>
        <Title class="task__name" :data="{
          title: 'Medical App (iOS native)',
          isHighLeading: true,
          size: 'medium',
        }"/>
      </div>
      <CircleProgressBar :data="{
          value: 32,
          max: 118,
          size: 24
        }"/>
    </div>
    <hr class="task__line">
    <Title :data="{
      title: 'Project Data',
      size: 'small',
      marginBottom: 'medium',
      isHighLeading: true
    }"/>
    <div class="task__overview">
      <div class="task__all-tasks">
        <div class="task__column-name">
          All tasks
        </div>
        <div class="task__column-data">
          34
        </div>
      </div>
      <div class="task__active-tasks">
        <div class="task__column-name">
          Active tasks
        </div>
        <div class="task__column-data">
          13
        </div>
      </div>
      <div class="task__assignees">
        <div class="task__column-name">
          Assignees
        </div>
        <Avatars :data="{}"/>
      </div>
    </div>
    <div class="task__info">
      <div class="task__date">
        <span class="task__data-text">
          Priority
        </span>
        <Priority :data="{
        priority: 'medium',
        isShowText: true
      }"/>
      </div>
      <div class="status">
        Done
      </div>
    </div>
  </article>
</template>

<script setup lang="ts">
import { type IBook } from 'src/entities/user'
import { Title } from '@/shared/ui/title'
import IconBase from "@/shared/ui/icon-base/ui/IconBase.vue";
import { Priority } from "@/shared/ui/priority";
import { CircleProgressBar } from "@/shared/ui/circle-progress-bar";
import { Avatars } from "@/shared/ui/avatars";

const props = defineProps<{
  data: IBook
}>()
</script>

<style lang="scss">
 @import "style.module";
 .status {
   border-radius: 8px;
   background: rgb(224, 249, 242);
   color: rgb(0, 208, 151);
   font-size: 12px;
   font-weight: 700;
   padding: 8px 16px;
   line-height: 16px;
 }
</style>
