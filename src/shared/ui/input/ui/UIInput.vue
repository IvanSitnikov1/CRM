<template>
  <article class="input__content">
    <label :for="data.name" class="label input__label">
      {{ data.title}}
    </label>
    <div class="input">
      <input
        class="input__text"
        :name="data.name"
        :id="data.name"
        :placeholder="data.placeholder"
        :type="data.type"
        :value="data.value"
        :required="data.isRequired"
        :readonly="data.isReadonly"
        @input="handlerInput"
      />
      <IconBase v-if="data.iconName"
                :data="{
                  iconName: data.iconName,
                  iconColor: data.iconColor
                }"
      />
    </div>

  </article>
</template>

<script setup lang="ts">
import { type IUIInput } from './../index'
import IconBase from "@/shared/ui/icon-base/ui/IconBase.vue";

const emit = defineEmits(['onInput'])

const props = defineProps<{
  data: IUIInput
}>()

const handlerInput = (event: InputEvent) => {
  emit('onInput', event?.target?.value || '')
}
</script>

<style lang="scss">
  @import "style.module";
</style>



