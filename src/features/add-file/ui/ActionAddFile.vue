<template>
    <ActionButton
        @click="open"
        :data="{
            iconName: 'search',
            color: '#6D5DD3',
        }"
    />
</template>

<script setup>
import { useFileDialog } from '@vueuse/core';
import { useAppModel } from '@/entities/app';
import { IconBase } from '@/shared/ui/icon-base';
import { ActionButton } from '@/shared/ui/action-button';

const { files, open, reset, onChange } = useFileDialog({
  accept: 'image/*', // Set to accept only image files
  directory: false
});

onChange(files => {
  console.log(files);
});

</script>

<style lang="scss">
  @import "style.module";
</style>
