<template>
  <article class="link">
    <router-link
      class="link__text"
      :title="data.title"
      :to="data.to">
      <IconBase
        v-if="data.iconLeft"
        :data="{
          iconName: data.iconLeft,
          iconColor: data.iconLeftColor
        }"
      />
      {{ data.title }}
      <IconBase
        v-if="data.iconRight"
        :data="{
          iconName: data.iconRight,
          iconColor: data.iconRightColor
        }"
      />
    </router-link >
  </article>
</template>

<script setup lang="ts">
import { type ILink } from './../index'
import IconBase from "@/shared/ui/icon-base/ui/IconBase.vue";

const props = defineProps<{
  data: ILink
}>()


</script>

<style lang="scss">
 @import "style.module";
</style>
