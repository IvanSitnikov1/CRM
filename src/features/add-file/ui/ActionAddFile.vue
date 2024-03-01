<template>
    <ActionButton
        @click="open"
        :data="{
            iconName: 'attach',
            color: '#6D5DD3',
        }"
    />
</template>

<script setup>
import { useFileDialog } from '@vueuse/core';
import { useAppModel } from '@/entities/app';
import { IconBase } from '@/shared/ui/icon-base';
import { ActionButton } from '@/shared/ui/action-button';
import { useToast } from 'vue-toastification'

const { files, open, reset, onChange } = useFileDialog({
  accept: 'image/*', // Set to accept only image files
  directory: false
});

const toast = useToast();


onChange(files => {
  toast.info("Файл успешно добавлен!")
});

</script>

<style lang="scss">
  @import "style.module";
</style>
