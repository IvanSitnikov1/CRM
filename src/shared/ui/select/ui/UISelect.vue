<template>
  <article>
    <label for="format" class="select__label">Request Subject</label>
    <div class="select__container">
      <select class="select" name="format" id="format" @focus="handleFocus" @blur="handleBlur">
        <option value="pdf">PDF</option>
        <option value="txt">txt</option>
        <option value="epub">ePub</option>
        <option value="fb2">fb2</option>
        <option value="mobi">mobi</option>
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
import { type ITag } from './../index'
import IconBase from "@/shared/ui/icon-base/ui/IconBase.vue";

const props = defineProps<{
  data: ITag
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
