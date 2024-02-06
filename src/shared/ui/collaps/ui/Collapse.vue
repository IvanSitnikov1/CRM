<template>
  <article class="collapse">
    <div class="collapse__header" @click="handlerExpanded(!isExpanded)">
      <slot name="header">
        <div class="collapse__header-default">
          <div class="collapse__arrow" :class="{ 'collapse__arrow_rotate': isExpanded}">
            <img src="@/shared/assets/icons/arrowDown.svg" alt="arrow">
          </div>
          <div class="collapse__title">
            Groups
          </div>
        </div>
      </slot>
    </div>

    <Collapse :when="isExpanded">
      <slot name="content"/>
    </Collapse>
  </article>
</template>

<script setup>
import { Collapse } from 'vue-collapsed'

const isExpanded = ref(false)

const handlerExpanded = (value) => {
  isExpanded.value = value
}
</script>

<style lang="scss">
 @import "styles.module";
</style>
