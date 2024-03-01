<template>
  <button
    class="action-button"
    :style="{ backgroundColor: data.color + '1A'}"
  >
    <IconBase
      :data="{
                iconName: data.iconName,
                iconColor: data.color
            }"
    />
  </button>
</template>

<script setup lang="ts">
import { IconBase } from "@/shared/ui/icon-base";
import type { IActionButton } from "@/shared/ui/action-button";

const props = defineProps<{
  data: IActionButton
}>()

</script>

<style lang="scss">
 @import "styles.module";
</style>
