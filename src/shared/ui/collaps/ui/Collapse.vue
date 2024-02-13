<template>
  <article class="collapse">
    <div class="collapse__header" @click="handlerExpanded(!data.isExpanded)">
      <slot name="header">
        <div class="collapse__header-default">
          <div class="collapse__arrow" :class="{ 'collapse__arrow_rotate': !data.isExpanded}">
            <img src="@/shared/assets/icons/arrowDown.svg" alt="arrow">
          </div>
          <div class="collapse__title">
            {{ data.title }}
          </div>
        </div>
      </slot>
    </div>
    <Collapse :when="data.isExpanded">
      <slot name="content"/>
    </Collapse>
  </article>
</template>

<script setup lang="ts">
import { Collapse } from 'vue-collapsed';

import { type ICollapse} from './../index'

const emit = defineEmits(['onExpanded'])

const props = defineProps<{
  data: ICollapse
}>()

const handlerExpanded = (value: boolean) => {
  emit('onExpanded', value)
}


</script>

<style lang="scss">
 @import "styles.module";
</style>
