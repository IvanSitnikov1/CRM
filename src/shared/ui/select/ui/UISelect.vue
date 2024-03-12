<template>
  <article>
    <label :for="data.name" class="label select__label">{{ data.title }}</label>
    <div class="select__container">
      <select class="select"
              :name="data.name"
              :id="data.name"
              :multiple="data.isMultipleSelect"
              @focus="handleFocus"
              @blur="handleBlur"
      >
        <option v-for="option in data.options"
                :value="option.value">
          {{ option.title }}
        </option>
      </select>
      <IconBase
        class="select__icon"
        :class="{'select__icon_open': state.isOpen}"
        :data="{
          iconName: 'arrowDown'
        }"
      />
    </div>
  </article>
</template>

<script setup lang="ts">
import { type ISelect } from './../index'
import IconBase from "@/shared/ui/icon-base/ui/IconBase.vue";

const props = defineProps<{
  data: ISelect
}>()

const state = reactive({
  isOpen: false
})

const handleFocus = () => {
  state.isOpen = true;
}

const handleBlur = () => {
  state.isOpen = false;
}

</script>

<style lang="scss">
 @import "styles.module";
</style>
