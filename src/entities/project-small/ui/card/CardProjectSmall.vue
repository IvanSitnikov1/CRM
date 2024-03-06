<template>
  <article class="project-small">
    <div class="project-small__body">
      <div class="project-small__info">
        <span class="project-small__id">
          {{ data.id }}
        </span>
        <Title class="project-small__name" :data="{
          title: data.title,
          isHighLeading: true,
          size: 'small',
          marginBottom: 'small'
        }"/>
        <Link :data="{
          title: 'View details',
          iconRight: 'arrowRight',
          to: '/projects/details'
        }"/>
      </div>
      <div class="project-small__select">
        <IconBase :data="{
          iconName: 'arrowDown'
        }"/>
      </div>
    </div>
  </article>
</template>

<script setup lang="ts">
import { Title } from '@/shared/ui/title'
import type { IProjectSmall } from '@/entities/project-small'
import { IconBase } from '@/shared/ui/icon-base'
import { Link } from '@/shared/ui/link'

const props = defineProps<{
  data: IProjectSmall
}>()

</script>

<style lang="scss">
 @import "style.module";
</style>
