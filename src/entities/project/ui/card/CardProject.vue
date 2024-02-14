<template>
  <article class="project" v-for="index in 3" :key="index">
    <div class="project__header">
      <div class="project__category">
        <img class="project__image" src="@/shared/assets/projectThemFirst.png" alt="icon">
      </div>
      <div class="project__meta">
        <div class="project__index">
          PN0001265
        </div>
        <Title class="project__name" :data="{
          title: 'Medical App (iOS native)',
          isHighLeading: true,
          size: 'medium',
        }"/>
      </div>
    </div>
    <div class="project__info">
      <div class="project__date">
        <IconBase :data="{
          iconName: 'calendar'
        }"/>
        <time class="project__data-text">
          Created Sep 12, 2020
        </time>
      </div>
      <Priority :data="{
        priority: 'medium',
        isShowText: true
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
  </article>
</template>

<script setup lang="ts">
import { type IBook } from 'src/entities/user'
import { Title } from '@/shared/ui/title'
import IconBase from "@/shared/ui/icon-base/ui/IconBase.vue";
import { Priority } from "@/shared/ui/priority";

const props = defineProps<{
  data: IBook
}>()
</script>

<style lang="scss">
 @import "style.module";
</style>
