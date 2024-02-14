<template>
  <article class="project" v-for="index in 3" :key="index">
    <div class="project__header">
      <div class="project__meta">
        <div class="project__index">
          Task Name
        </div>
        <Title class="project__name" :data="{
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
    <hr class="project__line">
    <Title :data="{
      title: 'Project Data',
      size: 'small',
      marginBottom: 'medium',
      isHighLeading: true
    }"/>
    <div class="project__overview">
      <div class="project__all-tasks">
        <div class="project__column-name">
          All tasks
        </div>
        <div class="project__column-data">
          34
        </div>
      </div>
      <div class="project__active-tasks">
        <div class="project__column-name">
          Active tasks
        </div>
        <div class="project__column-data">
          13
        </div>
      </div>
      <div class="project__assignees">
        <div class="project__column-name">
          Assignees
        </div>
        <div class="project__column-avatars">
          <div class="project__avatar" v-for="index in 2" :key="index">
            <img src="@/shared/assets/test.png" alt="assigned" class="project__avatar-image">
          </div>
          <div class="project__avatar project__avatar_last">
            +2
          </div>
        </div>
      </div>
    </div>
    <div class="project__info">
      <div class="project__date">
        <span class="project__data-text">
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
