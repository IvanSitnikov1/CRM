<template>
  <article class="add-file">
    <IconBase
      :data="{
        iconName: 'menu',
        iconColor: '#0A1629',
      }"
    />
  </article>
</template>

<script setup>
import { useAppModel } from '@/entities/app'
import { IconBase } from "@/shared/ui/icon-base";

const app = useAppModel()

</script>

<style lang="scss">
  @import "style.module";
</style>

