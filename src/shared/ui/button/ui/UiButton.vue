<template>
  <button class="button" :class="{'button_full': data.isFull }" :type="data.type">
    <IconBase v-if="data.iconNameLeft" :data="{
      iconName: ''
    }">
      <slot name="icon-left">
      </slot>
    </IconBase>
    <span class="button__text">
      {{ data.title }}
    </span>
    <IconBase v-if="data.iconNameRight" :data="{
      iconName: ''
    }">
      <slot name="icon-right">
      </slot>
    </IconBase>
  </button>
</template>

<script setup lang="ts">
import { type IButton } from './../index'
import IconBase from "@/shared/ui/icon-base/ui/IconBase.vue";

const props = defineProps<{
  data: IButton
}>()
</script>

<style lang="scss">
  @import "style.module";
</style>
