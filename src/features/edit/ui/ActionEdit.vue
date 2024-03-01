<template>
  <article class="edit">
    <IconBase
      @click="handlerTest"
      :data="{
        iconName: 'edit',
        iconColor: '#0A1629',
      }"
    />
  </article>
</template>

<script setup>
import { IconBase } from '@/shared/ui/icon-base';
import { useToast } from 'vue-toastification'


const toast = useToast();

const handlerTest = () => {
  toast.info("Можно будет изменить описание и т.д!")
}
</script>

<style lang="scss">
  @import "style.module";
</style>
