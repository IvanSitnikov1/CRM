<template>
  <article class="tag-time">
    <IconBase :data="{
            iconName: 'clock'
          }"/>
    <time class="event__date" >{{ data.time }}</time>
  </article>
</template>

<script setup lang="ts">
import IconBase from "@/shared/ui/icon-base/ui/IconBase.vue";
import type { ITagTime } from "@/shared/ui/tag-time";

const props = defineProps<{
  data: ITagTime
}>()

</script>

<style lang="scss">
 @import "styles.module";
</style>
