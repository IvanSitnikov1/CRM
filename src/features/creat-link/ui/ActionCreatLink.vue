<template>
    <ActionButton
        @click="handlerTest"
        :data="{
            iconName: 'link',
            color: '#15C0E6'
        }"
    />
</template>

<script setup lang="ts">
import { ActionButton } from '@/shared/ui/action-button';
import { useToast } from 'vue-toastification'

const toast = useToast();

const handlerTest = () => {
  toast.info("Пока не работает!")
};

</script>

<style lang="scss">
  @import "style.module";
</style>
