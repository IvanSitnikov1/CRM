<template>
  <article class="priority" :class="IconColorClass">
    <IconBase class="priority__icon"
              :data="{
                    iconName: 'priority',
                  }"
              :class="{'priority__icon_small': !data.priority || data.priority === 'small'}"
    />
    <span v-if="data.isShowText" class="priority__text">
      {{ state.text }}
    </span>
  </article>
</template>

<script setup lang="ts">
import { type IPriority } from "./../index";
import IconBase from "@/shared/ui/icon-base/ui/IconBase.vue";

const props = defineProps<{
  data: IPriority
}>()

const state = reactive({
  text: 'Small'
})

const IconColorClass = computed(() => {
  switch (props.data.priority) {
    case "large":
      state.text = 'Large'
      return 'priority_large'
    case "medium":
      state.text = 'Medium'
      return 'priority_medium'
    case "small":
      state.text = 'Small'
      return 'priority_small'
    default:
      return 'priority_small'
  }
})

</script>

<style lang="scss">
 @import "styles.module";
</style>
